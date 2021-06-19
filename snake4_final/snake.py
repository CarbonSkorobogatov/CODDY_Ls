import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode( (800, 600) )
clock = pygame.time.Clock()
SPEED = 30
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINTS = 0
font = pygame.font.SysFont(None, 32)

pygame.mixer.init()
game_music = pygame.mixer.Sound('./sound/gamesound.wav')
game_music.set_volume(0.3)
point_sound = pygame.mixer.Sound('./sound/point.wav')
point_sound.set_volume(0.2)

def score():
    global GAME_POINTS, COLOR
    text = font.render(f'Очки: {GAME_POINTS}', True, COLOR)
    text_rect = text.get_rect(center=(400, 500))
    screen.blit(text, text_rect)

def pickup():
    global apple_rect, head_rect, GAME_POINTS, snake

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(40, 740)
        apple_rect.y = randint(40, 560)
        GAME_POINTS += 10
        snake.append(snake[1].copy())
        point_sound.play()

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x,y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect

def gameover():
    global snake, head_rect
    for el in snake[1:]:
        if head_rect.colliderect(el):
            return True
    return False

def move(obj, snake):
    global DIRECTION, SPEED, COLOR, KEYS, GAME_POINTS

    if KEYS[K_UP] and DIRECTION[1] == 0:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] and DIRECTION[1] == 0:
        DIRECTION = [0, SPEED]
    elif KEYS[K_RIGHT] and DIRECTION[0] == 0:
        DIRECTION = [SPEED, 0]
    elif KEYS[K_LEFT] and DIRECTION[0] == 0:
        DIRECTION = [-SPEED, 0]

    if obj.bottom > 600:
        obj.top = 0
    elif obj.top < 0:
        obj.bottom = 600
    elif obj.left < 0:
        obj.right = 800
    elif obj.right > 800:
        obj.left = 0

    for i in range( (len(snake) - 1), 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i - 1].y

    obj.move_ip(DIRECTION)

head_image, head_rect = load_img('./img/head.png', 400, 300)
apple_image, apple_rect = load_img('./img/apple.png', 200, 200)
body_image, body_react = load_img('./img/body.png', 370, 300)

snake = [head_rect, body_react]

game_music.play()
Ispalay = True

while True:
    screen.fill( (0, 0, 0) )
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    if Ispalay:
        KEYS = pygame.key.get_pressed()
        screen.blit(head_image, head_rect)
        screen.blit(apple_image, apple_rect)
        pickup()
        score()
        for el in snake[1:]:
            screen.blit(body_image, el)
        move(head_rect, snake)

    if gameover():
        text = font.render(f'Игра окончена', True, COLOR)
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        Ispalay = False
        game_music.stop()

    pygame.display.update()
    clock.tick(10)