
# While

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break

print("continue")
i = 0
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i)


# For. Итерируем списки и словари

print("FOR")

l = [1, 2, 3, 4, 5]

for element in l:
    print(element)

d = {"key": "value",
     "another": "number"}

print("------------")
print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))
print("------------")


for item in d.items():
    print(f"Key: {item[0]}, Value: {item[1]}")

for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

for key in d.keys():
    print(f"Key: {key}")

for value in d.values():
    print(f"Value: {value}")

# range

for i in range(10, 0, -1):
    print(i)

# enumerate

for i, value in enumerate(["a", "b", "c"]):
    print(f"{i} {value}")
