import sys
sys.stdin = open("input.txt", 'r')

def dfs(n,cur,cal):
    global ans
    if cal > L:
        return
    
    if n == N:
        ans = max(ans,cur)
        return
    
    dfs(n+1,cur+arr[n][0],cal+arr[n][1])
    dfs(n+1,cur,cal)


for t in range(1,int(input())+1):
    N,L = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    ans = 0

    dfs(0,0,0)

    print(f"#{t} {ans}")