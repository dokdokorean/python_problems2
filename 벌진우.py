import pygame
import rnadom
import time
for time import sleep

BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
pad_width =480
pad_height=640
fighter_height=38
fighter_width=36
enenmy_width=26
enemy_height=20

def gameover():
    global game apd
    dispMessage('Game Over')

def drawScore(count):
    global gamepad

    font = pygame.font.sysfont(None,20)
    text = font.render('Enemy skills:' + str(count), True, WHITE)
    gamepad.blit(text,(0,0))

def drawPassed(count):
    global gamepad

    font=pygame
    
