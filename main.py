# See it in action
# https://www.youtube.com/watch?v=D7LCZXtDqbs

import pygame
from pygame import gfxdraw
import math
import random

pygame.init()  # needed to start pygame

screen = pygame.display.set_mode((1280,720))
screen2 = pygame.surface.Surface((1280,720),pygame.SRCALPHA)
screen3 = pygame.surface.Surface((1280,720),pygame.SRCALPHA)

pygame.mixer.music.load("assets/music/Monkeys-Spinning-Monkeys.mp3")
pygame.mixer.music.play(-1)
bubble = pygame.mixer.Sound("assets/sfx/mixkit-hard-pop-click-2364.wav")
tri = pygame.mixer.Sound("assets/sfx/mixkit-game-show-buzz-in-3090.wav")

#icon = pygame.image.load('game.jpg')
#pygame.display.set_icon(icon)
pygame.display.set_caption("It's just fuckin spots man")

done = False
font = pygame.font.SysFont('agencyfb', 50)

total = 0


# QoL function to truncate decimal to reasonable length
def truncate_to_decimals(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError("decimals places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimals must be greater than or equal to 0")
    if decimals == 0:
        return math.trunc(number)
    return math.trunc(number * 10.0 ** decimals) / 10.0 ** decimals


def message_to_screen(msg,color,layer):
    screenText = font.render(msg, True, color)
    textWidth = screenText.get_rect().width
    layer.blit(screenText,[(1280/2)-(textWidth/2),720/2])


def draw_circle(surface, x, y, r, color):
    gfxdraw.aacircle(surface, x, y, r, color)
    gfxdraw.filled_circle(surface, x, y, r, color)


def draw_triangle(surface, x, y):

    side = random.randint(5,400)
    height = truncate_to_decimals(((side * math.sqrt(3))/2), decimals=2)
    print(f"An equilateral with a side length of {side} will have a height of {height}")

    startPoint = (x-(side/2),y+(height/2))
    nextPoint = (startPoint[0]+(side/2),startPoint[1]-height)
    finalPoint = (startPoint[0]+side,startPoint[1])
    points = [startPoint,nextPoint,finalPoint]
    print(points)

    pygame.draw.polygon(surface, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), points, 0)


while not done:

    message_to_screen("Just make spots man.", (255,255,255),screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            draw_circle(screen2, x, y, random.randint(5,200), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            screen.blit(screen2,[0,0])
            bubble.play()

            #score counter adds one if circle is drawn
            total += 1
            draw_circle(screen3,640,390,50, (255,255,255))
            message_to_screen(str(total),(255,0,0),screen3)
            screen.blit(screen3,[-550,-300])

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = pygame.mouse.get_pos()
            print(x,y)
            draw_triangle(screen2, x, y)
            screen.blit(screen2,[0,0])
            tri.play()

            #score counter subtracts one if circle is drawn
            total -= 1
            draw_circle(screen3,640,390,50, (255,255,255))
            message_to_screen(str(total),(255,0,0),screen3)
            screen.blit(screen3,[-550,-300])

    pygame.display.flip()
