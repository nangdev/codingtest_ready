def solution(land):
    dp = land[0]

    for l in range(1,len(land)):
        for i in range(4):
            temp = land[l][i]
            land[l][i] = -1
            dp[i] += max(land[l])
            land[l][i] = temp
    
    return max(dp)


def solution2(land):

    for i in range(1, len(land)):

        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    
        print(land[i])
    return max(land[-1])


print(solution2([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))


#앞으로 가는거랑 뒤로 가는거랑 값이 다름 