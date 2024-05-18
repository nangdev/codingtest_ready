import sys
sys.stdin = open("input.txt", 'r')

for t in range(1, int(input())+1):
    n,m = map(int,input().split())
    fee = [[0,True] for _ in range(n)]
    for i in range(n):
        fee[i][0] = int(input())

    weight = []
    for _ in range(m):
        weight.append(int(input()))
    
    arr = []
    for _ in range(m*2):
        arr.append(int(input()))
    
    ans = 0

    wait = []

    for a in arr:
        if a > 0: # 들어오는 경우
            for f in fee:
                chk = False
                if f[1] == True:
                    f.append(weight[a-1])
                    chk = True
                    f[1] = False
                    break

            if not chk:
                wait.append(weight[a-1])
        
        else: #음수인 경우
            for f in fee:
                if f[1] == False and f[2] == weight[-a-1]:
                    ans += weight[-a-1] * f[0]
                    f[1] = True
                    f.pop()

                    if wait:
                        f.append(wait.pop(0))
                        f[1] = False
                    
                    break
    
    print(f"#{t} {ans}")