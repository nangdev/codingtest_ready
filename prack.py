import sys
from collections import deque
sys.stdin = open("input.txt", 'r')

t = int(input())
for i in range(1, t+1):
    N, A, B = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    arr = deque(arr)
    min_val, max_val = arr.popleft(), arr.pop()

    while arr[0] == min_val:
        arr.popleft()

    while arr[-1] == max_val:
        arr.pop()

    lis = []

    for a in range(1, arr[-1]+1):
        lis.append(arr.count(a))

    print(lis)
    ans = 0
    temp = lis[0]
    for li in range(1, len(lis)):
        if temp+lis[li] <= B:
            temp += lis[li]
        else:
            ans = temp
            temp = lis[li]

    if temp > ans:
        ans = temp

    print(f"#{i} {ans}")
