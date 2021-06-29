import pygame as pg
from pygame.locals import *

BALLSPEED = 10

class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.score = 0
        self.isMoving = True
        self.speedX = BALLSPEED
        self.speedY = BALLSPEED * -1

    def update(self, keys, platform, *args):
        if self.isMoving:
            self.rect.y += self.speedY

            hitGroup = pg.sprite.Group(platform)
            spriteHitList = pg.sprite.spritecollide(self, hitGroup, False)

            if len(spriteHitList) > 0:
                self.speedY *= -1
                self.rect.y += self.speedY
            elif (self.rect.bottom > 600):
                self.speedY *= -1
                self.rect.top = 0

            self.rect.x += self.speedX

            if self.rect.right > 800:
                self.speedX *= -1
                self.rect.right = 800

            if self.rect.left < 0:
                self.speedX *= -1
                self.rect.left = 0

            if self.rect.top < 0:
                self.speedY *= -1
                self.rect.top = 0

class Platform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((60, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(400, 590))

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
        self.platform = Platform()
        ball = Ball()
        self.spites.add(self.platform)
        self.spites.add(ball)

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
        screen.fill((0,0,0))
        self.spites.update(keys, self.platform)
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
