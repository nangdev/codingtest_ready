def solution(A,B):
    sortA = sorted(A)
    sortB = sorted(B, reverse=True)

    ans = 0

    for i in range(len(A)):
        ans += sortA[i] * sortB[i]
    
    return ans