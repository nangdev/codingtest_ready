import sys
sys.stdin = open("input.txt", 'r')

for t in range(1,int(input())+1):

    N = int(input())
    arr = list(map(int,input().split())) + [0]
    ans = 0

    sell = []
    val = max(arr)
    for a in range(N):
        if arr[a] == val:
            for s in sell:
                ans += val-s
            
            val = max(arr[a+1:])
            sell.clear()
        
        else:
            sell.append(arr[a])

    print(f"#{t} {ans}")