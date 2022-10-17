import pygame

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Brick Breaker')

FPS = 60


class Paddle:
    VEL = 5

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


def draw(win):
    win.fill('white')
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(win)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
