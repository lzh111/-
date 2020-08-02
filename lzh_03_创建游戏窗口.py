import pygame
#初始化
pygame.init()

#创建窗口 set_mode(resolution=(0,0),flags=0,depth=0)
'''
resolution 指定屏幕的宽和高
flags  参数指定屏幕的附加选项 例如是否全屏 
depth 参数表示颜色的位数  默认自动匹配
'''

screen=pygame.display.set_mode((480,700))

# 绘制背景图像 要在屏幕上看到一个图像的内容
#1.加载图像的数据
bg=pygame.image.load("./images/background.png")
#2.使用游戏屏幕对象调用blit方法将图像绘制到指定位置
screen.blit(bg,(0,0))
#3.调用pygame.display.update()更新整个屏幕的显示
pygame.display.update()


pygame.quit()

