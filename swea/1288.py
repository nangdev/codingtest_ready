import sys
sys.stdin = open("input.txt",'r')

for test in range(1,int(input())+1):
    N = int(input())
    
    arr = set()

    i = 1
    temp = []
    while len(arr) != 10:
        temp = str(N * i)
        
        for t in temp:
            arr.add(t)
        
        i += 1
    
    ans = "".join(temp)
    
    print(f"#{test} {ans}")