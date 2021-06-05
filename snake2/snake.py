import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode( (800, 600) )
clock = pygame.time.Clock()
SPEED = 10
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINTS = 0
font = pygame.font.SysFont(None, 32)

def score():
    global GAME_POINTS, COLOR
    text = font.render(f'Очки: {GAME_POINTS}', True, COLOR)
    text_rect = text.get_rect(center=(400, 500))
    screen.blit(text, text_rect)

def pickup():
    global apple_rect, head_rect, GAME_POINTS

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(40, 740)
        apple_rect.y = randint(40, 560)
        GAME_POINTS += 10

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x,y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect

def move(obj):
    global DIRECTION, SPEED, COLOR, KEYS, GAME_POINTS

    if KEYS[K_UP]:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN]:
        DIRECTION = [0, SPEED]
    elif KEYS[K_RIGHT]:
        DIRECTION = [SPEED, 0]
    elif KEYS[K_LEFT]:
        DIRECTION = [-SPEED, 0]
    elif KEYS[K_w]:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_s]:
        DIRECTION = [0, SPEED]
    elif KEYS[K_d]:
        DIRECTION = [SPEED, 0]
    elif KEYS[K_a]:
        DIRECTION = [-SPEED, 0]
    elif KEYS[K_SPACE]:
        DIRECTION = [0, 0]

    if obj.bottom > 600:
        obj.top = 0
    elif obj.top < 0:
        obj.bottom = 600
    elif obj.left < 0:
        obj.right = 800
    elif obj.right > 800:
        obj.left = 0

    obj.move_ip(DIRECTION)

head_image, head_rect = load_img('./img/head.png', 400, 300)
apple_image, apple_rect = load_img('./img/apple.png', 200, 200)

while True:
    screen.fill( (0, 0, 0) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)
    move(head_rect)
    pickup()
    score()
    pygame.display.update()
    clock.tick(30)