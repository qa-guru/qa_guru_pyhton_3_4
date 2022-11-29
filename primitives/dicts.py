
# Заводим словарики

d = {"key": "value", "user_id": 123, "dict": {"key": "value"}}
print(d["key"])
# print(d["unexpected"])
print(d["user_id"])
print(d["dict"]["key"])


# Функции словарей

print(d.get("unexpected", "default"))