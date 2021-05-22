x = [10, 10, 20, "asd"]
print(x)
print(x.__sizeof__())
print( type(x) )
del x[1]
print(x)
y = (10, 10, 20, "asd")
print(y[0])
print(y.__sizeof__())
print( type(y) )
a = tuple( (1,2,3,4,5,6,67) )
print(a)

