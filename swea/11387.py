import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    D,L,N = map(int,input().split())

    damg = 0

    for i in range(N):
        damg += int(D*(1+(N * ((L/100)))))
    
    print(f"#{t} {damg}")