import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    N,K = map(int,input().split())
    arr = []
    grade = ['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
    for _ in range(N):
        a,b,c = map(int,input().split())
        arr.append((a * 35) + (b* 45) + (c * 20))
    
    temp = arr[K-1]
    arr.sort()

    ans = grade[arr.index(temp)//(N//10)]
    
    print(f"#{t} {ans}")