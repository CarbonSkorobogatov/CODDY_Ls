N = int(input("Введите положительное число: "))
if N > 0:
	i = 0
	sum = 0
	while i < N:
		if i%2 == 0: sum += i
		i += 1
	print("sum = ", sum)
else: print("Число ", N, " меньше 0")

input("Enter")