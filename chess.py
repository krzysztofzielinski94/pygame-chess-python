import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Chess')
icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(icon)

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    