def solution(n, computers):
    ans = 0
    v = [0] * n

    def dfs(num):
        v[num] = 1
        for com in range(n):
            if num != com and computers[num][com] == 1 and v[com] == 0:
                dfs(com)

    for i in range(n):
        if v[i] == 0:
            dfs(i)
            ans += 1

    return ans