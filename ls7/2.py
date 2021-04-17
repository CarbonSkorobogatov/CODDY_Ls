str = "Hello, World! My name is Sviatoslav"
str1 = list(str)
str1.remove("!")
text = ""
for i in range(0, len(str1)): text = text + str1[i]
print(text)
str2 = str.split()
str2.remove("Sviatoslav")
print(str2)
input()