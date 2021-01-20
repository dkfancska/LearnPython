x = int(input())
y = int(input())

z = (x - y) ** 2
z = z ** 0.5
max_num = int((x + y + z) / 2)
print(max_num)
