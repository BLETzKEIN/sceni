import random

import pygame


def spaace():
    rect.right = random.randint(0, 800)
    rect.top = random.randint(0, 600)

def smena_sceni():
    global scena
    if scena == "rect":
        scena = "ellipse"
    else:
        scena = "rect"

def right():
    global x
    x+=10

def left():
    global x
    x-=10



rect = pygame.Rect([100, 100], [200, 100])
x = 100
y = 50
scena = "rect"
