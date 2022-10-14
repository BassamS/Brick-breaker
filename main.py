import pygame

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Brick Breaker')


def draw():
    win.fill('white')
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
