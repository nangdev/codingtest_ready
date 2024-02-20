N = int(input())
for i in range(N):
    arlen = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    cursor = arr[0]
    count = 1
    while cursor < arlen:
        count += 1
        cursor += arr[cursor]
    
    print(count)