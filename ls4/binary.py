a = int(input("Введите ваше число а: "))
p = 100 

while a != p:
	p = p // 2
	print(p)
	if(p > a): 
		i = p//2
		p +=i
	else:  	
		i = p//2
		p -=i

input("Для выхода из программы нажмите ENTER")