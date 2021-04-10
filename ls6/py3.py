from random import randint
x = [1,2,3,4,5]
print(x[1:4])
print("-----------------------")

list1 = []
for i in range(0, 11, 1): list1.append(randint(0,100))
print(list1)
print("-----------------------")

list2 = list1
k = len(list2)
for j in range(0, k, 1): list2.pop()
print(list2)
print("-----------------------")

input()

