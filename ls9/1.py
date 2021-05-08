import pygame #Импорт библиотеки с которой будем работаем
from sys import exit

WHITE = (255, 255, 255)

pygame.init() #Инициализация библитеки
screen = pygame.display.set_mode((800, 900)) #Создания окна и уставка его размеров
pygame.display.set_caption("First Pygame's Application") #Устанавливаем имя окна
FPS = 60
frame = pygame.time.Clock()
life = True #Переменнная описывающая жизнь программы

pygame.draw.polygon( screen, (122, 120, 150), ((10,10), (790, 10), (790, 890)))
pygame.draw.circle( screen, WHITE, (400, 200), 100)

while life: #Тело игры
    for e in pygame.event.get(): #Обработчик событий
        if e.type == pygame.KEYUP: #Проверка события событий
            pygame.quit()       #Выход
            exit()
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update() #Обновление события
    frame.tick(FPS)