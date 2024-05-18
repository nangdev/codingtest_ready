import sys
sys.stdin = open("input.txt", 'r')

for t in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split())) # 2N
    ans = []

    i = 0
    while i < len(arr):
        temp = arr[i]
        if (temp//3) * 4 in arr[i:]:
            ans.append(temp)
            arr.remove(temp//3 * 4)
        i += 1

    print(f"#{t} ", end='')
    print(*ans)