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

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt)
    pygame.draw.circle(screen, color, pt, thick)

# HW2 implement drawLine with drawPoint


def drawLine(pt0, pt1, color='GREEN', thick=3):
    # Native Implementation
    """
    steps = 1e-2
    a1 = 0

    while a1 <= 1:
        a0 = 1-a1
        drawPoint(
            (a0 * pt0[0] + a1 * pt1[0], a0 * pt0[1] + a1 * pt1[1]), # a0 * p0 + a1 * p1
            color,
            thick
        )
        a1 += steps
    """
    # Numpy Implementation
    A = np.array([pt0, pt1]).T
    # Generate a0 and a1, with constraint a0 + a1 = 1 and a0, a1 >= 0
    #a = np.linspace((0, 1), (1, 0), num=100).T
    dist = np.linalg.norm(A[:,0] - A[:,1])
    a0 = np.arange(0, 1, 1 / dist)
    a1 = 1 - a0
    a = np.array([a0, a1])

    XY = np.dot(A, a).T  # Coords for points on the line between pt0 and pt1

    for x, y in XY:
        drawPoint((x, y), color, thick)


def drawPolylines(points, color='GREEN', thick=3):
    if len(points) < 2:
        return
    for i in range(len(points)-1):
        drawLine(points[i], points[i+1], color, thick=1)


def drawPolyLines2(points, color='GREEN', thick=3):
    if len(points) < 2:
        return
    drawLine(points[-2], points[-1], color, thick)


# Loop until the user clicks the close button.
done = False
margin = 6
pts = []

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    button = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = (x, y)
    pygame.draw.circle(screen, RED, pt, 0)

    print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y) +
          " button:"+repr(button[0])+" pressed:"+repr(button))

    if button[0]:
        pts.append(pt)
        pygame.draw.rect(
            screen, BLUE, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        drawPolyLines2(pts, GREEN, 1)
        print("Add points ...")

    elif button[2]:
        pts.clear()
        screen.fill(WHITE)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()

pygame.quit()