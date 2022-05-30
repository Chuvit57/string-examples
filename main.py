string = "Hello friends"
# print(string)
# print(string[4])
# print(string[:-1])
# print(len(string))
# print(string[1:13:2])
# exist = "Hello" in string
# print(exist)
# for char in string:
#   print(char, end="|*|")
# print()
# Methods string
a = string.isalpha() # Возвращает True если строка состоит только из алфавитных символов
print(a)

b = " 123456710 "
print(b)
print(type(b))
print(b.isdigit())

string1 = "Стоимость программного обеспечения рассчитывается индивидуально. "
print(string1.title())
print(string1.strip('Ст'))  # Команда возвращает копию строки с удаленными начальными и конечными символами.

# lstrip() возвращает копию строки с удаленными начальными символами.
website = 'https://campus.datacamp.com '
my_string = "I control github"
print(website.lstrip('htps://'))

# Метод rstrip() возвращает копию строки с удаленными конечными символами.
print(website.rstrip('.com'))

# Метод ljust() возвращает выровненную по левому краю строку заданной минимальной ширины: string.ljust(width[, fillchar])
width = 36
fill_char = '%'
print(website.ljust(width, fill_char))
print(len(website))

print(website.center(width, fill_char))
print(website.center(width))
print(b.center(width))
print(b.center(width, '+'))
print(my_string.center(width, '^'))


# isnumeric() Возвращает флаг, указывающий на то, содержит ли строка только числа.
print(b.isnumeric())