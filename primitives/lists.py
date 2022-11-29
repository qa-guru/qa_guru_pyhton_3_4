
# Делаем списки!

l = [1, 2, 3, 4, 5, "a", "b", "c", [1, 2, 3]]

print(l[0])
print(l[::-1])
l[0] = 10
l[-1][1] = "abc"


# Функции списков

len(l)

ll = [1, 2, 3, 4, 5, 10, 2, 5, 2.5]
ll.sort(reverse=False)
print(ll)
new_list = sorted(ll, reverse=True)
print(new_list)

# Множества

s1 = set([1, 2, 3, 3, 3, 3, 4, 5])
s2 = {1, 2, 3, 3, 3, 3}
s3 = {1, 2, "3", "4"}
print(s3)
