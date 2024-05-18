import sys
sys.stdin = open("input.txt", 'r')

for t in range(1,int(input())+1):
    st = list(map(int,input()))
    ans = 0 
    cur = 0

    for i in range(len(st)):
        if st[i] != 0:
            if cur >= i:
                cur += st[i]
            else:
                ans += i-cur
                cur += i-cur+st[i]

    
    print(f"#{t} {ans}")