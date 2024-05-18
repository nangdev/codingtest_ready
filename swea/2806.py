def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    
    for i in range(N):
        if v[i] == 0 and v2[n+i] == 0 and v3[n-i] == 0:
            v[i] = 1
            v2[n+i] = 1
            v3[n-i] = 1
            dfs(n+1)
            v[i] = 0
            v2[n+i] = 0
            v3[n-i] = 0




for t in range(1,int(input())+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    ans = 0
    v = [0] * (2*N)
    v2 = [0] * (2*N) 
    v3 = [0] * (2*N)

    dfs(0)

    print(f"#{t} {ans}")