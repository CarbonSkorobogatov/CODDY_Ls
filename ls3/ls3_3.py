from random import randint

x = randint(-10,100)
y = randint(-10,1)
z = randint(-10,100)

print("x = ", x, " y = ", y, "z = ", z)

if x > 0:
	print("x>0")
else:
	print("x<0")

if y > 0:
	print("y>0")
else:
	print("y<0")

if z > 0:
	print("z>0")
else:
	print("z<0")

end = input("Для выхода из программы нажмите ENTER")