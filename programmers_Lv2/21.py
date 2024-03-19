def solution(n, left, right):
    ans = []

    lval = left//n
    rval = right//n

    for i in range(lval,rval+1):

        for j in range(i+1):
            ans.append(i+1)
        
        val = i+1
        for k in range(n-i-1):
            val += 1
            ans.append(val)

    start = left % n
    offset = right-left
    
    return ans[start:start+offset+1]


print(solution(4,7,14))