import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N = int(input())

    chk = False
    breakchk = False

    for i in range(1,10):
        for j in range(1,10):
            if i*j == N:
                chk = True
                breakchk = True
                break
        if breakchk:
            break
    
    if chk:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")