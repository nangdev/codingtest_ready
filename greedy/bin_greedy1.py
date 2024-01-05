n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
lis = []
for i in range(2):
    temp = max(arr)
    lis.append(temp)
    arr.remove(temp)

for j in range(m):
    if j != 0 and j % k == 0:
        ans.append(lis[1])
        continue
    ans.append(lis[0])

print(sum(ans))