import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    offset = N-M+1

    for i in range(offset):
        for j in range(offset):
            sumval = 0
            for k in range(M):
                sumval += sum(arr[i+k][j:j+M])
            ans = max(ans,sumval)


    print(f"#{t} {ans}")