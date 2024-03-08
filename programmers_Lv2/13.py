def solution(people, limit):
    global ans
    arr = sorted(people)
    N = len(arr)
    ans = limit

    def dfs(n,cur):

        if n == N:
            ans = min(ans,cur)
        
        if people[n] + people[n+1] <= limit:
            dfs(n+1,cur+1)

