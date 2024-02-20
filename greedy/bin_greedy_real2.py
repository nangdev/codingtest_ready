N = int(input())
for i in range(N):
    arr = list(map(int,input()))
    result = arr[0]
    for j in range(1,len(arr)):
        if result * arr[j] > result + arr[j]:
            result *= arr[j]
        else:
            result += arr[j]
    
    print(result)