import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N,K = map(int,(input().split()))
    arr = list(map(int,(input().split())))

    ans = 0

    arr.sort()

    for i in range(1,K+1):
        ans += arr[-i]

    print(f"#{t} {ans}")