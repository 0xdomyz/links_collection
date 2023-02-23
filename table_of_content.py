with open("program.rst") as f:
    lst = f.readlines()

lst2 = []
for i in range(len(lst)):
    if lst[i].startswith("----"):
        lst2.append(lst[i - 1])

print(lst2)

[print(i.strip()) for i in lst2]
