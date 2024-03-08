def solution(n, words):
    num = 0
    temp = []
    check = True

    for i in words:
        num += 1
        
        # 첫번째 단어라면 처리해줌 두번째 조건에서 인덱스 오류남 이거안하면면
        if num == 1:
            if len(i) != 1:
                temp.append(i)
                continue
            else:
                break

        # 이어지지 않거나 이미 말했던 단어거나 글자가 한단어라면 종료
        if temp[-1][-1] != i[0] or i in temp or len(i) == 1:
            check = False
            break

        temp.append(i)

    print(num)

    if num == len(words) and check:
        return [0, 0]
    else:
        if num % n == 0:
            return [n, num//n]
        else:
            return [num % n, num//n + 1]