from collections import deque

def isRight(s):
    stack = []

    for i in s:
        if stack and i == ']':
            if stack[-1] == '[':
                stack.pop()
        elif stack and i == '}':
            if stack[-1] == '{':
                stack.pop()
        elif stack and i == ')':
            if stack[-1] == '(':
                stack.pop()
        else:
            stack.append(i)
    
    return stack

def solution(s):
    q = deque(s)
    N = len(s)
    ans = 0

    for i in range(N):
        temp = q.popleft()
        q.append(temp)

        string = "".join(q)

        if not isRight(string):
            ans += 1
    
    return ans