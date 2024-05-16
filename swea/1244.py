import sys
sys.stdin = open("input.txt",'r')


for t in range(1,int(input())+1):
    N,K = input().split()
    arr = list(map(int,N))
    K = int(K)
    re = sorted(arr, reverse=True)
    cnt = 0


    ans = "".join(arr)
    print(f"#{t} {ans}")