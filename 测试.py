import pygame,sys
from pygame.locals import *

pygame.init()

windowsSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello new world!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None,44)

text = basicFont.render('Hello new world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowsSurface.get_rect().centerx
textRect.centery = windowsSurface.get_rect().centery

windowsSurface.fill(RED)

pygame.draw.polygon(windowsSurface, GREEN, ((146, 0), (291, 106), (236, 277), (0, 106)))

pygame.draw.circle(windowsSurface, BLACK, (200, 0), 20, 0)

pygame.draw.ellipse(windowsSurface, BLACK, (300, 250, 40, 80), 1)

pygame.draw.rect(windowsSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(windowsSurface)
pixArray[480][380] = WHITE

delpixArray

windowsSurface.blit(text, textRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()