import pygame

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Brick Breaker')


def main():
    run = True
    while run:
        for event in pygame.event.get()
        if event.type == pygame.QUIT:
            run = False
            break
