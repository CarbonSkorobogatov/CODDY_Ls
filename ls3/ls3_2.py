#Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его. Вывести полученное число.
from random import randint

x = randint(-10,100)
y = randint(-10,100)
z = randint(-10,100)

print("x = ", x, " y = ", y, "z = ", z)

if x > 0 and z > 0 and y > 0: print("All is more than 0")
else: print("nop")

end = input("Для выхода из программы нажмите ENTER")