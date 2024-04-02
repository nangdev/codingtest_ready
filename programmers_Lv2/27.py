def solution(s):
    answer = []
    arr = []

    stack = []
    num = ""
    for i in range(1, len(s)-1):
        if s[i].isdigit():
            num += s[i]
        
        elif s[i] == ",":
            if num:
                stack.append(int(num))
                num = ""
        
        elif s[i] == '}':
            if num:
                stack.append(int(num))
                num = ""
            arr.append(stack[:])
            stack.clear()

    arr = sorted(arr, key=lambda x: len(x))

    for ar in arr:
        for ans in ar:
            if ans not in answer:
                answer.append(ans)
    
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
