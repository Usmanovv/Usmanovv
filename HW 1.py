from re import S
import pygame
from sys import exit
import numpy as np
    
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

background_image_filename = 'image/curve_pattern.png'

background = pygame.image.load(background_image_filename).convert()
width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

old_pt = np.array([0, 0])
cur_pt = np.array([0, 0])
old_rect = np.array([0,0])

screen.fill(WHITE)

clock= pygame.time.Clock()

done = False
pressed = -1
margin = 6
while not done:   

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = 1            
        elif event.type == pygame.MOUSEMOTION:
            pressed = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 2            
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = -1

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    cur_pt = np.array([x, y])

    if pressed == 1:
        if button1 == 1:
            pygame.draw.rect(screen, BLUE, (cur_pt[0]-margin, cur_pt[1]-margin, 2*margin, 2*margin), 5)
            if old_rect[0] > 0 and old_rect[1] > 0:
                pygame.draw.line(screen, GREEN, old_rect, cur_pt, 5)
            old_rect = np.array([x, y])
        elif button3 == 1:
            pygame.draw.rect(screen, RED, (cur_pt[0]-margin, cur_pt[1]-margin, 2*margin, 2*margin), 5)
            if old_rect[0] > 0 and old_rect[1] > 0:
                pygame.draw.line(screen, GREEN, old_rect, cur_pt, 5)
            old_rect = np.array([x, y])
        elif button2 == 1:
            pygame.draw.rect(screen, BLACK, (cur_pt[0]-margin, cur_pt[1]-margin, 2*margin, 2*margin), 5)
            if old_rect[0] > 0 and old_rect[1] > 0:
                pygame.draw.line(screen, GREEN, old_rect, cur_pt, 5)
            old_rect = np.array([x, y])

    print("mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" "+repr(button2)+" "+repr(button3)+" pressed:"+repr(pressed))
    old_pt = cur_pt   

    pygame.display.update()

pygame.quit()
