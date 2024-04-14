def solution(dirs):
    answer = 0
    arr = [[0]* 11 for _ in range(11)]
    cx,cy = 5,5
    
    for i in dirs:
        if i == "U" and cx-1 >= 0:
            if arr[cx][cy] + arr[cx-1][cy] <= 1:
                answer += 1
            arr[cx-1][cy] = 1
            cx -= 1

        elif i == "R" and cy + 1 < 11:
            if arr[cx][cy] + arr[cx][cy+1] <= 1:
                answer += 1
            arr[cx][cy+1] = 1
            cy += 1

        elif i == "D" and cx+1 < 11:
            if arr[cx][cy] + arr[cx+1][cy] <= 1:
               answer += 1
            arr[cx+1][cy] = 1
            cx += 1
           
        elif i == "L" and cy -1 >= 0:
            if arr[cx][cy] + arr[cx][cy-1] <= 1:
                answer += 1
            arr[cx][cy-1] = 1
            cy -= 1

    return answer


print(solution("ULURRDLLU"))
