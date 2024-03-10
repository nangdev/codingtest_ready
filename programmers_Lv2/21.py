def solution(n, left, right):
    l, r = 0, 0

    for i in range(n):

        if n*i <= left < n*i+n:
            l = i

        if n*i <= right < n*i+n:
            r = i

    ltemp = []
    midtemp = []
    rtemp = []

    for lval in range(l*n,(l+1)*n):
        if lval < lval + +l+1:
            

        

