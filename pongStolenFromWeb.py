from time import sleep
from sense_hat import SenseHat
import pygame
from pygame.locals import *
import threading
 
sense = SenseHat()
sense.clear(0,0,0)
 
pygame.init()
pygame.display.set_mode((320, 240))
y = 4
ball_position=[6,3]
ball_speed=[-1,-1]
 
def drawbat():
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)
 
def moveball():
    global game_over
    while True:
        sleep(0.5)
 
        sense.set_pixel(ball_position[0],ball_position[1],0,0,0)
 
        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]
 
        if ball_position[1] == 0 or ball_position[1] == 7:
            ball_speed[1] = -ball_speed[1]
        if ball_position[0] == 7:
            ball_speed[0] = -ball_speed[0]
        if ball_position[0] == 1 and y-1 <= ball_position[1] <= y+1:
            ball_speed[0] = -ball_speed[0]
        if ball_position[0] == 0:
            break
 
        sense.set_pixel(ball_position[0],ball_position[1],0,0,255)
 
    game_over = True
 
game_over = False
 
thread = threading.Thread(target=moveball)
thread.start()
 
while not game_over:
    drawbat()
 
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP and y > 1:
                sense.set_pixel(0,y+1,0,0,0)
                y -= 1
            if event.key == K_DOWN and y < 6:
                sense.set_pixel(0,y-1,0,0,0)
                y += 1
 
sense.show_message("You Lose", text_colour=(255,0,0))