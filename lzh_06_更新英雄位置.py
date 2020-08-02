import pygame
from plane_sprites import  *
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

#绘制英雄的飞机
hero=pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))
pygame.display.update()

#创建时钟对象
clock=pygame.time.Clock()

#定义rect记录飞机的初始位置
hero_rect=pygame.Rect(150,300,102,126)


#创建敌机的精灵
enemy=GameSprite("./images/enemy1.png")
enemy1=GameSprite("./images/enemy1.png",2)

#创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)

while True:
    #可以指定循环体内部代码执行的频率
    clock.tick(60)

    #捕获事件
    # event_list=pygame.event.get()
    # if len(event_list)>0:
    #     print(event_list)
    #

    #事件监听
    for event in pygame.event.get():
        #判断用户是否点击了关闭按钮
        if event.type==pygame.QUIT:
            print("退出系统")
            pygame.quit()

            exit()#直接终止当前程序

    #2.修改飞机的位置
    hero_rect.y-=1
    if hero_rect.y<=-126:
        hero_rect.y=700
    #3.调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)


    #让精灵组调用两个方法
    #update
    enemy_group.update()
    #draw
    enemy_group.draw(screen)

    #4.调用update方法更新显示
    pygame.display.update()

pygame.quit()

