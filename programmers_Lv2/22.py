def solution(citations):
    citations.sort()
    for c in range(len(citations)):
        N = len(citations[c:])

        if N <= citations[c]:
            return N 
    
    return 0


print(solution([0,0,0,0,0]))