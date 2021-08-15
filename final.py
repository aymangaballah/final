# This is a sample Python script.
#functions for color

def water_blue():
    pygame.draw.rect(window,BLUE, (x,y, width, hight))
    pygame.display.update()
def wight ():
    pygame.draw.rect(window, WIGHT, (x, y, width, hight))
    pygame.display.update()
def green ():
    pygame.draw.rect(window, GREEN, (x, y, width, hight))
    pygame.display.update()
def gray ():
    pygame.draw.rect(window, GRAY, (x, y, width, hight))
    pygame.display.update()
def bridge():
    if xm in range(600, 700) and ym in range(300, -400):
        pygame.time.delay(200)
        pygame.display.set_caption("yes")
def checkmove():
    if move==endMove:
        window.fill((0,0,0))
        pygame.quit()
        exit()

# the function that draw the background
def make_squar():
    global x
    x=0
    global y
    y=0
    for i in range(0, col):
        for j in range(0, row):
            if i in range(1, 6) and j in range(1, 6):
                wight()
                y += 102
                checkmove()
                continue
            if i == 6 and j == 3:
                green()
                y += 102
                continue
            water_blue()
            y += 102
        x += 102
        y = 0

import random
from random import randint

def movement1 ():
    checkmove()
    global xm  # x for mouse only
    global ym  # y for mouse only
    key = pygame.key.get_pressed()
    if (disc==1) and xm+width+step<=720:
        key[pygame.K_RIGHT]
        xm+=104
        move+1
        checkmove()
    if(disc==2) and xm-step>=0:
        key[pygame.K_LEFT]
        xm-=104
        move+1
        checkmove()
    if (disc==3) and ym-step>=0:
        key[pygame.K_UP]
        ym-=104
        move+1
        checkmove()
    if (disc==4) and ym+hight+step<=720:
        key[pygame.K_DOWN]
        ym+=104
        move+1

    pygame.display.update()

def movement2():
    checkmove()
    global xm  # x for mouse only
    global ym  # y for mouse only
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and xm+width+step<=720:
        xm+=104
    if key[pygame.K_LEFT] and xm-step>=0:
        xm-=104
    if key[pygame.K_UP] and ym-step>=0:
        ym-=104
    if key[pygame.K_DOWN] and ym+hight+step<=720:
        ym+=104

    pygame.display.update()

#define pygame and other variables

import pygame
pygame.init()
window=pygame.display.set_mode((720,720))
#image = pygame.transform.scale(image, (desired_width,desired_height))
mouse= pygame.image.load("mouse.png")
pygame.display.set_caption("mouse&cat")
icon=pygame.image.load("mouse.png")
pygame.display.set_icon(icon)
#set the mouse to a small size
mouse=pygame.transform.scale(mouse,(60,60))
xm = 0 # x for mouse only
ym =0 # y for mouse only
width=100
hight=100
BLUE=(0,102,153)
WIGHT=(255,255,255)
GREEN=(0,230,0)
GRAY=(128,128,128)
row,col=(7,7)
list=("")
step=100
move=0
endMove=20
list_cat=[110,210,310,410,510]
i=random.choice(list_cat)
j=random.choice(list_cat)
def cat():
    cat_pic=pygame.image.load("cat.jpg")
    cat_pic = pygame.transform.scale(cat_pic, (97,97))
    window.blit(cat_pic, (i, j))
#the start or running code
pygame.display.update()

while True:
 pygame.time.delay(150)
 cat()
 make_squar()
 cat()
 checkmove()
 window.blit(mouse, (xm, ym))
 disc = randint(1, 4)

 for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        exit()

 movement1()
 movement2()












