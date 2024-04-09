def solution(word):
    words = ['A','E','I','O','U']
    
    arr = []

    for a in words:
        arr.append(a)
        for e in words:
            w = a+e
            arr.append(w)
            for i in words:
                w = a+e+i
                arr.append(w)
                for o in words:
                    w = a+e+i+o
                    arr.append(w)
                    for u in words:
                        w = a+e+i+o+u
                        arr.append(w)
    
    arr.sort()
    
    return arr.index(word)+1


print(solution("I"))
