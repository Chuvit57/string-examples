string = "Hello friends"
print(string)
print(string[4])
print(string[:-1])
print(len(string))
print(string[1:13:2])
exist = "Hello" in string
print(exist)
for char in string:
  print(char, end="|*|")
print()
# Method string
a = string.isalpha()
print(a)