import pygame
from pygame.locals import *
from sys import exit
from random  import randint

pygame.init()
pygame.display.set_caption("Snake")

head = Rect(400, 300, 30, 30)
screen = pygame.display.set_mode( (800, 600) )
clock = pygame.time.Clock()
SPEED = 10
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)

def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def move(obj):
    global DIRECTION, SPEED, COLOR, KEYS

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

    if obj.bottom > 600:
        DIRECTION = [0, -SPEED]
        COLOR = rand_color()
    elif obj.top < 0:
        DIRECTION = [0, SPEED]
        COLOR = rand_color()
    elif obj.left < 0:
        DIRECTION = [SPEED, 0]
        COLOR = rand_color()
    elif obj.right > 800:
        DIRECTION = [-SPEED, 0]
        COLOR = rand_color()

    obj.move_ip(DIRECTION)


while True:
    #screen.fill( (0, 0, 0) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    KEYS = pygame.key.get_pressed()
    pygame.draw.rect(screen, COLOR, head)
    move(head)
    pygame.display.update()
    clock.tick(30)