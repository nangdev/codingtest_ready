import sys
sys.stdin = open("input.txt", 'r')

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    
    ans = 0

    for i in range(N):
        wei, nuwei = arr[i][0], arr[i][0]
        val, nuval = arr[i][1], arr[i][1]
        for j in range(N):
            if j == i:
                continue
            
            if wei + arr[j][0] <= K:
                ans = max(ans,val+arr[j][1])
            
            if nuwei + arr[j][0] <= K:
                nuwei += arr[j][0]
                nuval += arr[j][1]
            else:
                ans = max(ans,nuval)

    print(f"#{t} {ans}")