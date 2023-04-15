import pygame
import model

def events ():
    b = pygame.event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.KEYDOWN:
            if s.key == pygame.K_SPACE:
                model.spaace()