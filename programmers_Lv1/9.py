def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    arr = list(zip(survey, choices))

    for i in arr:
        cur = ""
        cho = 0
        if i[1] > 4:
            cur = i[0][1]
            cho = i[1]-4
        elif i[1] < 4:
            cur = i[0][0]
            if i[1] == 1:
                cho = 3
            elif i[1] == 2:
                cho = 2
            else:
                cho = 1
        else:
            continue

        dic[cur] += cho

    result = ""
    alp = [["R","T"],["C","F"],["J","M"],["A","N"]]
    for a in alp:
        if dic[a[0]] >= dic[a[1]]:
            result += a[0]
        else:
            result += a[1]
    
    return result


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))