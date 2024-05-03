def solution(dartResult):
    ans = []

    cur = ""

    for i in dartResult:
        if i.isdigit():
            if type(cur) is str:
                cur += i

            else:
                ans.append(cur)
                cur = ""
                cur += i

            continue

        elif i.isalpha():
            cur = int(cur)
            if i == "D":
                cur = cur ** 2
            elif i == "T":
                cur = cur ** 3
            continue

        else:
            if i == "*":
                cur *= 2
                if ans:
                    ans[-1] *= 2
            elif i == "#":
                cur *= -1

    ans.append(cur)
    print(ans)

    return sum(ans)


print(solution("1S*2T*3S"))
