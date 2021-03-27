x = 0
sum = 0
	
#continue
#break

while x <= 100: 
	if sum > 1000: 
		print("more then 1000 wit x =  ", x)
		break

	sum += x
	x += 1

print("sum = ", sum)
input("Для выхода из программы нажмите ENTER")