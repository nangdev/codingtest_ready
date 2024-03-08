def solution(n):
    a = format(n,'b').count('1')

    for i in range(n+1, 1000000):
        if a == format(i,'b').count('1'):
            return i