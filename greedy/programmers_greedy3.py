# def solution(num, k):
#     def dfs(n, prob):
#         if n == N:
#             if len(prob) == N-k:
#                 print(prob)
#                 ans = max(ans, prob)
#             return

#         for j in range(N):
#             if v[j] == 0:
#                 v[j] = 1
#                 dfs(n+1, prob+num[n])
#                 v[j] = 0


#     N = len(num)
#     v = [0]*N
#     ans = '0'

#     dfs(0, "")
#     return ans

# print(solution("1924",2))

def solution(num,k):

    N = len(num)
    ans = '0'
    
    def dfs(n,prob):
        nonlocal ans
        if len(prob) > N-k:
            return

        if n==N:
            if len(prob) == N-k:
                ans = max(ans,prob)
            return
        
        if len(prob) < N-k:
            dfs(n+1, prob+num[n])
        
        dfs(n+1,prob)
        

    dfs(0,'')
    return ans