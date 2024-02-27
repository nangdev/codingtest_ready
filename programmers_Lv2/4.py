def solution(s):
    stack = []
    for i in s:
        if i == ")" and stack and stack[-1] == "(":
            stack.pop()
            continue
        stack.append(i)
    
    if stack:
        return False
    else:
        return True