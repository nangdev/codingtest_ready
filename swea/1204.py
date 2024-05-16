import sys
sys.stdin = open("input.txt",'r')

for t in range(int(input())):
    T = int(input())
    arr = list(map(int,input().split()))
    ans = 0

    temp = set(arr)
    dic = {}

    for i in temp:
        dic[i] = arr.count(i)
    
    arr2 = sorted(dic.items(), key= lambda x:x[1], reverse=True)
    
    print(f"#{T} {arr2[0][0]}")