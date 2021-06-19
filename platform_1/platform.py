import pygame as pg
from pygame.locals import *


class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60, 10))
        self.rect = self.image.get_rect(center=(400, 590))
        self.image.fill((255, 0, 0))

    def update(self, keys, *args):
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 15
        if keys[K_d] and self.rect.x < 740:
            self.rect.x += 15


class Game:
    def __init__(self):
        self.score = 0
        self.game_over = 0
        self.spites = pg.sprite.Group()
        platorfm = Platform()
        self.spites.add((platorfm))

    def process_events(self):
        for e in pg.event.get():
            if e.type == QUIT:
                return True
            if e.type == MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

    def run_logic(self):
        pass

    def display_frame(self, screen, keys):
        screen.fill( (0,0,0) )
        self.spites.update(keys)
        self.spites.draw(screen)


def main():
    pg.init()

    pg.display.set_caption("Game 2")
    screen = pg.display.set_mode( (800, 600) )
    endgame = False

    clock = pg.time.Clock()
    game = Game()

    while not endgame:
        endgame = game.process_events()
        game.run_logic()
        key = pg.key.get_pressed()
        game.display_frame(screen, key)

        pg.display.update()
        clock.tick(60)

if __name__ == "__main__": main()
