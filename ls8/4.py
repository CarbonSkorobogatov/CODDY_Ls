def circle(r):
    return 3.14 * r ** 2
def three(n):
    if n % 3 == 0: return True
    return False
def maxList(mylist):
    k = mylist[0]
    for i in range(0, len(mylist)):
        if mylist[i] > k: k = mylist[i]
    return k
def evenCounter(myList):
    k = 0
    for i in range(0, len(myList)):
        if myList[i] % 2 == 0: k += 1
    return k
def unique(myList):
    listner = []
    for i in range(0, len(myList)):
        if listner.count(myList[i]) == 0: listner.append(myList[i])
    return listner
def more(x, y):
    if x>y: return x
    elif y>x: return y
    return "x = y"
def sqrts(x):
    return x*x
def listnera(a, b):
    c = []
    if len(a) != len(b): return -1
    for i in range(0, len(a)):
        c.append(a[i] + b[i])
    return c


mylist = [1, 1, 2, 1, 3, 2, 3, 4, 4,4 , 4, 6, 6, 6, 6, 5, 4, 3, 0]
print(maxList(mylist))
evens = evenCounter(mylist)
print(evens)
print(unique(mylist))
print("--------------------------")
print(more(1,1))
print(sqrts(4))

print("--------------------------")
print(listnera([1,2,3], [2,4,2]))