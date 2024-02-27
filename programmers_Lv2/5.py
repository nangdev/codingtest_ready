def solution(s):
    zero = 0
    count = 0

    while s != "1":
        x = ""

        for i in s:
            if i == "1":
                x += i
            else:
                zero += 1

        x = format(len(x), 'b')
        count += 1

        s = x
        x = ""
    
    return [count,zero]