names = [["Sviatoslav", 2, 2, 2], ["Alex.azu", 10, 10, 10], ["Develope_Man", 10, 10, 10], "farum", "Bohdan", "Valeia", "Vladimir"]


print(names[0].count(2))
k = names[0].count(2)
for i in range(0, k, 1): names[0].remove(2) 
print(names[0])
input()