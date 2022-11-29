
# Объявляем функции и аргументы

# Возвращаем значение

# Переменное количество аргументов

# Переменное количество возвращаемых значений

# Функция - тоже объект

def by_age(d):
    return d["age"]

by_age({"name": "Oleg", "age": 32})

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

print(sorted(users, key=by_age))
