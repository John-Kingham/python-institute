import pygame


def setup_screen() -> None:
    height: int
    width: int
    height_margin: int
    width_margin: int
    screen: pygame.Surface
    text: pygame.Surface

    width = 400
    height = 100
    screen = pygame.display.set_mode((width, height))
    text = setup_text()
    width_margin = (width - text.get_width()) // 2
    height_margin = (height - text.get_height()) // 2
    screen.blit(text, (width_margin, height_margin))
    pygame.display.flip()


def setup_text() -> pygame.Surface:
    font: pygame.font.Font
    white: tuple[int, int, int]

    font = pygame.font.SysFont(None, 48)
    white = (255, 255, 255)
    return font.render("Welcome to pygame", True, white)


def main() -> None:
    run: bool = True

    pygame.init()
    setup_screen()
    while run:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP):
                run = False


if __name__ == "__main__":
    main()
