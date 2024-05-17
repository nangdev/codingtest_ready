import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    st = input()
    dic = {}
    ans = ""

    for s in set(st):
        dic[s] = 0
    
    for s in st:
        dic[s] += 1
    
    for s in set(st):
        if dic[s] % 2 == 0:
            continue
        else:
            ans += s
    
    ans = "".join(sorted(list(ans)))

    if ans == "":
        print(f"#{t} Good")
    else:
        print(f"#{t} {ans}")