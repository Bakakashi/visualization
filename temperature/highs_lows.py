import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 获取文件sitka_weather_07-2014.csv最高气温数据
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        

# 绘制数据
fig = plt.figure(dpi = 300, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)

# 标准化图像
plt.title("Daily high temperatures, July 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which='major', labelsize = 16)

plt.savefig('Daily high temperatures of July 2014 in sitka.png', bbox_inches = 'tight')
plt.show()


# 获取文件sitka_weather_2014.csv最高气温数据
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
        

# 绘制数据
fig = plt.figure(dpi = 300, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# 标准化图像
plt.title("Daily high temperatures-2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which='major', labelsize = 16)

plt.savefig('Daily high temperatures of 2014 in sitka-high-low-fill.png', bbox_inches = 'tight')
plt.show()


# 获取文件death_valley_2014.csv最高气温数据
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:    # 测试程序
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 绘制数据
fig = plt.figure(dpi = 300, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# 标准化图像
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which='major', labelsize = 16)

plt.savefig('Daily high temperatures of 2014 in Death Valley.png', bbox_inches = 'tight')
plt.show()