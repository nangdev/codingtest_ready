def solution(k, dungeons):
    global ans
    def dfs(n, cur, cnt):
        global ans
        if n == N:
            ans = max(ans, cnt)
            return

        if cur >= dun[n][0]:
            dfs(n+1, cur-dun[n][1], cnt+1)
        dfs(n+1, cur, cnt)

    ans = 0

    dun = sorted(dungeons, key=lambda x: x[0]-x[1], reverse=True)
    N = len(dun)

    dfs(0,k,0)

    return ans





print(solution(80, [[80, 20], [50, 40], [30, 10]]))
