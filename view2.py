import pygame
import model

display = pygame.display.set_mode([800, 600])


def weiv():
    display.fill([0, 0, 0])
    # pygame.draw.rect(display, [54, 97, 134], model.rect)
    pygame.display.flip()
