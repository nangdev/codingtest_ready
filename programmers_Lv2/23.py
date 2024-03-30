def solution(arr1, arr2):
    N = len(arr1)
    yarr = []

    for i in zip(*arr2):
        yarr.append(i)
    
    ans = [[] for _ in range(N)]
    
    for j in range(N):
        for k in range(len(yarr)):
            val = 0
            for x in range(len(arr1[0])):
                val += arr1[j][x] * yarr[k][x]
            
            ans[j].append(val)
        
    return ans