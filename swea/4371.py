import sys
sys.stdin = open("input.txt", 'r')

for t in range(1,int(input())+1):
    N = int(input())
    arr= []
    for _ in range(N):
        arr.append(int(input()))

    ans = 0
    offset = []
    for i in range(1,N):
        chk = True
        for o in offset:
            if arr[i]-o in arr:
                chk = False
                break

        if chk:            
            offset.append(arr[i]-1)
            ans += 1
    
    print(f"#{t} {ans}")