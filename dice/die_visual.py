import pygal
from die import Die

# 创建六面骰子 D6.
die = Die()

# 掷几次骰子，将结果存储在一个列表
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 结果可视化
hist = pygal.Bar()      # 柱状直方图

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')   # 存储为svg文件，用web打开
