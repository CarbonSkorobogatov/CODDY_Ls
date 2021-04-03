n = int(input("Enter number: "))

for i in range(0, n+1): 
	if i%3 == 0: print(i)

print("------------------")

for j in range(0, n+1, 3): 
	print(j)

input("Enter")