def solution(arr):
    rearr = []
    coparr = []

    # 원소 복사(그냥 대입하면 참조값 겹쳐서 수정사항 반영됨)
    for l in arr:
        coparr += [l]

    l = len(arr)
    count = 0

    for i in [2,3,5,7]:
        temp = []

        for j in coparr:
            if j % i == 0:
                temp.append(j//i)
        
        # 다 나눠졌다면
        if l == len(temp):
            rearr += [i]
            count += 1
            # 나눈 원소들로 포문에 리스트를 교체
            coparr = temp

    ans = 1
    # 2 3 5 7 중에 하나라도 다 나눠진 경우
    if count >= 1:
        for k in rearr:
            ans *= k
    # 공약수가 없는 경우
    else:
        for k in arr:
            ans *= k


    return ans

print(solution([]))