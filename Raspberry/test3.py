import RPi.GPIO as GPIO
import time
import pygame
import sys
import car_move as cm


car = cm.Move()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
car.initStart()
car.stop()

while True:#start
    # clock.tick(60)

    for event in pygame.event.get():#获取当前事件的队列
        if event.type == pygame.KEYDOWN:
            key_input = pygame.key.get_pressed()  # 可以同时检测多个按键
            #判断当前是在什么状态下前行
            if  key_input[pygame.K_w] and not key_input[pygame.K_a] and not key_input[pygame.K_d]:
                car.goStraight(car.speed)
            elif key_input[pygame.K_a]:
                car.turnLeft(40)
            elif key_input[pygame.K_d]:
                car.turnRight(40)
            elif key_input[pygame.K_s]:
                car.goBack(70)
            elif key_input[pygame.K_e]:
                car.stop()
            elif key_input[pygame.K_q]:
                car.exitAndClean()
                exit(1)
            elif key_input[pygame.K_UP]:
                car.speed += 20
            elif key_input[pygame.K_DOWN]:
                car.speed -= 20
            elif key_input[pygame.K_r]:
                car.speed = 70
        elif event.type == pygame.KEYUP:
            car.stop()
