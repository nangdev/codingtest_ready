num = 2932
n = list(str(num))
n.sort()
print(n)
a = ''.join(n[0:3:2])
b = ''.join(n[1:4:2])
print(a)
print(b)

print(int(a) + int(b))
