import pygame
import model

display = pygame.display.set_mode([800, 600])


def weiv():
    display.fill([0, 0, 0])
    # pygame.draw.rect(display, [54, 97, 134], model.rect)
    pygame.draw.ellipse(display,[89,56,92],[400,0,model.x,model.y])
    pygame.display.flip()
