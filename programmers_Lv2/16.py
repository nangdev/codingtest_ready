def dfs(num):
    global ans,k
    if num > k:
        return

    if num == k:
        ans += 1
        return

    dfs(num+1)
    dfs(num+2)


def solution(n):
    global ans,k
    k = n
    ans = 0
    
    dfs(0)

    return ans % 1234567

print(solution(4))