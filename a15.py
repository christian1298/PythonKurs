list = ["0023", "-11", "7"]

print(list)
list.sort(key=lambda x: abs(int(x)))
print(list)