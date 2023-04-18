import pygame
import model


def events():
    b = pygame.event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.KEYDOWN:
            if s.key == pygame.K_LEFT:
                model.left()
            if s.key == pygame.K_RIGHT:
                model.right()
            if s.key == pygame.K_ESCAPE:
                model.smena_sceni()
