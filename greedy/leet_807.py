grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
arr = []
n = len(grid[0])
lis = []

for i in range(n):
    a = max(grid[i])
    for j in range(n):
        b = 0
        for l in range(n):
            b = max(b,grid[l][j])
        
        lis.append(min(a,b))

ans = 0
print(lis)
for k in grid:
    ans += sum(k)

print(sum(lis) - ans)



