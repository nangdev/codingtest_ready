def solution(numbers, target):
    global ans
    ans = 0
    N = len(numbers)

    def dfs(n, cur):
        global ans

        if n == N:
            if cur == target:
                ans += 1
            return

        dfs(n+1, cur+numbers[n])
        dfs(n+1, cur-numbers[n])

    dfs(0, 0)

    return ans

# 10분 20초