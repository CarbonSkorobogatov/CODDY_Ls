A = int(input("Введите число А: "))

if A > 9999: 
	print("Valid number")
else:  
	x1 = A//1000
	x2 = A//100 % 10
	x3 = A%100 //10
	x4 = A%10
	print(x1, x2, x3, x4)
	
	if(x1 == x4 and x2 == x3):
		print("poli number")
	else: 
		print("not poli number")

end = input("Для выхода из программы нажмите ENTER")