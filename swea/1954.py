import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    j,k = 0,N-1
    offset = N-1

    for temp in range(N):
        arr[0][temp] = temp+1

    chk = True
    val = N+1
    while offset != 0:
        
        if chk:
            for a in range(offset):
                arr[j+1][k] = val
                val += 1
                j += 1
            
            for b in range(offset):
                arr[j][k-1] = val
                val += 1
                k -= 1
            
            chk = False
            offset -= 1
        
        else:
            for a in range(offset):
                arr[j-1][k] = val
                val += 1
                j -= 1
            
            for b in range(offset):
                arr[j][k+1] = val
                val += 1
                k += 1
            
            chk = True
            offset -= 1

            
    print(f"#{t}")
    for n in range(N):
        print(*arr[n])
