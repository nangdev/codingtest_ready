n = int(input())

if n % 2 == 0:
    print(3 ** (n//2) % 10007)
else:
    print(((3 ** (n//2)) * ((n//2)+(n % 2))) % 10007)
