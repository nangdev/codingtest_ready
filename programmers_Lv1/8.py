def solution(numbers, hand):
    answer = ''
    lval = [1, 4, 7]
    rval = [3, 6, 9]
    curL, curR = 7, 9

    for i in numbers:
        if i == 0:
            i = 10

        if i in lval:
            answer += 'L'
            curL = i
        elif i in rval:
            answer += 'R'
            curR = i
        else:
            temR = curR-2
            chkL = i - curL
            chkR = temR - i

            if chkL < chkR:
                answer += 'R'
                curR = i
            elif chkL > chkR:
                answer += 'L'
                curL = i
            elif chkL == chkR:
                if hand == "right":
                    answer += 'R'
                    curR = i
                else:
                    answer += "L"
                    curL = i

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
