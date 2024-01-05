n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

ans = []

for k in arr:
    ans.append(min(k))

print(max(ans))