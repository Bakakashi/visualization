import matplotlib.pyplot as plt
from random_walk import RandomWalk

index = 1
# 程序处于活动状态，不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # 设置绘图窗口分辨率与尺寸
    plt.figure(dpi = 300, figsize = (10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers,
                cmap = plt.cm.RdBu_r, edgecolor = 'none', s = 1)
        
    # 突出起点与终点
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', 
                edgecolors = 'none', s = 50)
        
    # 移除坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
       
    # 保存绘制图像
    png_name = str(index) + '.png'
    plt.savefig(png_name, bbox_inches = 'tight')
    
    # 显示绘制图像
    # plt.show()
    
    # 是否模拟多次随机漫步
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    else:
        index += 1
