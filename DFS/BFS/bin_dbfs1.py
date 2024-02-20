def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    
    return False

N,M = map(int, input().split())
ice = []
for _ in range(N):
    ice.append(list(map(int,input())))

result = 0 

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result += 1

print