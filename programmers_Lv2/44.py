def solution(numbers):
    lis = []

    for i in numbers:
        lis.append(str(i))

    lis.sort(key=lambda x:x*3,reverse=True)

    answer = ''

    for l in lis:
        answer += l

    return str(int(answer))