from random import randint

x = randint(-10,100)
y = randint(-10,100)

if x > y: print(x, " > ", y, " первое число больше второго")
elif x == y: print(x, " == ", y, " первое число равно второму")
else: print(y, " > ", x, " второе число больше первое")

end = input("Для выхода из программы нажмите ENTER")

