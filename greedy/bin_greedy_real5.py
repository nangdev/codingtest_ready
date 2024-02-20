N = int(input())
for i in range(N):
    M,K = map(int,input().split())
    arr = list(map(int,input().split()))
    result = 0

    for j in range(len(arr)):
        for k in range(j,len(arr)):
            if arr[j] == arr[k]:
                continue
            else:
                result += 1
    
    print(result)
