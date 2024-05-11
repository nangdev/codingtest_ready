def solution(sizes):
    big = []
    small = []

    for s in sizes:
        if s[0] > s[1]:
            big.append(s[0])
            small.append(s[1])
        else:
            big.append(s[1])
            small.append(s[0])
    
    return max(big) * max(small)