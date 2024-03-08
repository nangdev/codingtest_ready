def solution(brown, yellow):
    arr = []
    summ = brown + yellow

    for i in range(1,summ+1):
        if summ % i == 0:
            arr.append(i)
    
    # 약수의 갯수가 짝수
    if len(arr) % 2 == 0:
        # 큰게 앞임 가로가 더 큼
        return [arr[len(arr)//2], arr[len(arr)//2 - 1]]
    else:
        # 홀수면 가운데 원소 제곱임
        return [arr[len(arr)//2], arr[len(arr)//2]]


def solution2(brown,yellow):
    arr = []


    for i in range(1,yellow+1):
        if yellow % i == 0:
            arr.append(i)
    
    lenarr = len(arr)
    
    for j in range(lenarr//2):
        if len(arr) == 1:
            a,z = arr[0],arr[0]
        else:
            a,z = arr.pop(0), arr.pop()
        
        print(arr)
        
        if (z+2)*2 + a*2 == brown:
            return [z+2,a+2]
        

