def solution(name):
    leng = len(name)
    ans = leng-1
    for i in range(leng):
        if name[i] == 'A':
            continue
        elif ord(name[i])-65 <= 13:
            ans += ord(name[i]) - 65
        else:
            ans += ord('Z')-ord(name[i]) + 1

    if name[1:leng-1].count('A') == leng-2:
        ans -= leng-2
    return ans


name = "AAAAAB"

print(solution(name))

# 총 26개의 알파벳
# A = 65
