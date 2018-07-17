# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, 
                        print_function, unicode_literals)
# from urllib.request import urlopen
import json
import pygal
import math
from itertools import groupby

# 绘制收盘价均值
def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    # 将x轴与y轴数据合并、排序、然后再用groupby分组
    for x, y in groupby(sorted(zip(x_data, y_data)), key = lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])   # 求出每组均值
    # 将x轴与y轴数据分离
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

## 获取json数据
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# req = response.read()
# 将数据写入文件
# with open('btc_close_2017.json', 'wb') as f:
#     f.write(req)
# file_urllib = json.load(req)

# 将数据加载到一个列表
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# 打印每天的信息
for btc_dict in btc_data:
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
            btc_dict['date'], btc_dict['month'], int(btc_dict['week']),
            btc_dict['weekday'], int(float(btc_dict['close']))))

# 创建列表，存储日期与收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每天信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(btc_dict['month'])
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    
# 绘制折线图
line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels = False)
line_chart.title = '收盘价 (RMB) '
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
# line_chart.add('收盘价', close)
# line_chart.render_to_file('收盘价折线图(RMB).svg')
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图(RMB).svg')
    
# 收盘价月日均值图绘制
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month],
                             '收盘价月日均值(RMB)', '月日均值')
# 收盘价周日均值图绘制
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[:idx_week], close[:idx_week],
                             '收盘价周日均值(RMB)', '周日均值')
# 收盘价星期均值图绘制
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
      'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week],
                               '收盘价星期均值(RMB)', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四',
                               '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值(RMB).svg')

# 收盘价数据仪表盘
with open('收盘价Dashboard.html', 'w', encoding = 'utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图(RMB).svg',
            '收盘价对数变换折线图(RMB).svg',
            '收盘价月日均值(RMB).svg',
            '收盘价周日均值(RMB).svg',
            '收盘价星期均值(RMB).svg'
                ]:
        html_file.write('    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')