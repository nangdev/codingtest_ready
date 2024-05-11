def solution(numbers):
    arr = set()

    for i in numbers:
        arr.add(i)
        for j in numbers:
            arr.add(i+j)

    answer = 0
    print(arr)
    for i in arr:
        i = int(i)
        if i == 0 or i == 1:
            continue

        cnt = 0
        for j in range(2,i+1):
            if i % j == 0:
                cnt += 1
            
        if cnt == 1:
            answer += 1

    return answer

print(solution("17"))