# file_name = "program.rst"
# file_name = "pi.rst"
# file_name = "python_package_dev.rst"
file_name = "python.rst"

with open(file_name) as f:
    lst = f.readlines()

lst2 = []
for i in range(len(lst)):
    # if lst[i].startswith("----"):
    # if lst[i].startswith("===="):
    if lst[i].startswith("^^^^"):
        lst2.append(lst[i - 1])

print(lst2)

[print(i.strip()) for i in lst2]
