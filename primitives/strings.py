
# Учимся писать строки!

s = "Привет, мир!"
s = 'hello, world!'
s = """hello, world!"""
s = '''hello, world!'''
s = '''hello,""" world!'''
s = " ' "
s = ' " '
s = """ " ' """
s = "hello,  \"world!\" "

ss = "Hello, " \
     "world!"
ss = "Hello, \nworld!"
ss = """Hello, 
fslafhasf
fsakhflksahf
fsaljfalsjf
world!"""
print(s)


# Сырые строки

# Индексы и слайсы

abc = "abcdef"

c = abc[0]

print(abc[0])
print(abc[-1])
# print(abc[10])
print(abc[0:5])
print(len(abc))

print(abc[::-1])

print("https://google.com/"[8:-1])
# Оперируем

s = "Hello, world!"

print(s.lower())
print(s.upper())

# Форматируем

name = "Vasya"
a = "Hello, "
print(a + name)
print(f"{a}!!! {name.upper()}")
print("{}!!! {}".format(a, name))
print("{first}!!! {second}".format(first=a, second=name))
print("Форматирование: %s %s" % (a, name))

# Строку в число, и наоборот

number = 123
s = "123"

assert number == int(s)
assert str(number) == s

# int("1234flajsifihlask")
