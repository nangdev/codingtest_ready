from collections import Counter


def solution(topping):
    answer = 0

    arr = set()
    arr2 = Counter(topping)

    for i in topping:
        arr.add(i)

        arr2[i] -= 1

        if arr2[i] == 0:
            del arr2[i]

        if len(arr) == len(arr2):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
