def solution(clothes):
    dic = {}

    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = []

    for c in clothes:
        dic[c[1]].append(c[0])
    
    ans = 0
    N = len(dic)
    v = [0] * N

    def dfs(n,cur):
        if n == N:
            ans += 1
            return
        
        for i in range(N):
            



    

print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
