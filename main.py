import os
import pygame
from FractalTree import FractalTree, Point

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
    pygame.display.init()
    pygame.display.set_caption("Fractal Tree")
    pygame.key.set_repeat(5)
    size = Point(650, 650)
    screen = pygame.display.set_mode(size)
    tree = FractalTree(screen, 45, 1, 2);
    while tree.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tree.running = False
            if event.type == pygame.KEYDOWN:
                tree.kbin(event.key)
        if tree.update:
            screen.fill(0)
            tree.draw(Point(size.x / 2, size.y), -90, size.x // 2)
            pygame.display.update()

if __name__ == "__main__":
    main()
