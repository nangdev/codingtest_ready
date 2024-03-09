def solution(n,a,b):
    count = 1

    while a//2 + a % 2 != b//2 + b%2:
        count +=1
        a = a//2 + a%2
        b = b//2 + b%2
    
    return count