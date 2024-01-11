def solution(people, limit):
    people.sort()
    arr = []
    ans1, ans2 = 0, 0
    n = len(people)

    # 앞에서 부터 차례대로 비교

    for i in people:
        arr.append(i)
        if len(arr) == 2 and sum(arr) <= limit:
            ans1 += 1
            arr.clear()
        elif len(arr) == 2 and sum(arr) > limit:
            ans1 += 2
            arr.clear()

    # 홀수면 원소가 남아있을 수 있음
    if len(arr) != 0:
        ans1 += 1

    # 맨앞 맨뒤 비교

    r_idx, l_idx = 0, -1

    while r_idx < n//2:
        if people[r_idx] + people[l_idx] <= limit:
            ans2 += 1
        else:
            ans2 += 2

        r_idx += 1
        l_idx -= 1

    # 홀수면 하나 더해야함
    if n % 2 == 1:
        ans2 += 1

    return min(ans1, ans2)
