def solution(n, lost, re):
    los = sorted(lost)
    reser = sorted(re)
    count = 0

    for i in los:
        for j in reser:
            if i-j == 1 or i-j == -1:
                reser.remove(j)
                count += 1
                break
        if len(reser) == 0:
            break

    return n-(len(los)-count)


n = 5
lost = [3,5]
re = [2,5]

print(solution(n, lost, re))