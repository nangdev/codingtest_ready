s = "RLRRLLRLRL"

arr = []
ans = 0

for i in s:
    arr.append(i)
    if arr.count('R') == arr.count('L'):
        ans += 1
        arr.clear()

print(ans)
