def solution(n):
    i,a,b = 1,0,1
    num = 0

    while i != n:
        
        num = a+b
        a = b
        b = num
        i += 1
    
    return num % 1234567