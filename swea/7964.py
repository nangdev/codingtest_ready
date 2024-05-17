import sys
sys.stdin = open("input.txt", 'r')

for t in range(1, int(input())+1):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        lchk = False
        for j in range(1, D):
            if i-j >= 0:
                if arr[i-j] == 1:
                    lchk = True
            if lchk:
                break

        if not lchk:
            if arr[i-D] == 0:
                ans += 1
                arr[i-D] = 1

        rchk = False
        for j in range(1, D):
            if i+j < N:
                if arr[i+j] == 1:
                    rchk = True
            if rchk:
                break

        if not rchk:
            if i+D < N and arr[i+D] == 0:
                ans += 1
                arr[i+D] = 1

    print(f"#{t} {ans}")
