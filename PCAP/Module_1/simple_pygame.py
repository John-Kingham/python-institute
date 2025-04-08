import pygame

run: bool = True
width: int = 400
height: int = 100
font: pygame.font.Font
screen: pygame.Surface
white: tuple[int, int, int] = (255, 255, 255)
text: pygame.Surface

pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, white)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP):
            run = False
