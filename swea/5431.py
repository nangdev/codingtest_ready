import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    ans = []

    for i in range(1,N+1):
        if i in arr:
            continue
        else:
            ans.append(i)
    
    ans.sort()

    print(f"#{t} ",end="")
    print(*ans)