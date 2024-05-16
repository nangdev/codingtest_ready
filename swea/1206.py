import sys
sys.stdin = open("input.txt", 'r')

for t in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for b in range(2, N-2):
        if arr[b] <= arr[b-1] or arr[b] <= arr[b-2] or arr[b] <= arr[b+1] or arr[b] <= arr[b+2]:
            continue
        lmax = max(arr[b-1], arr[b-2])
        rmax = max(arr[b+1], arr[b+2])
        ans += arr[b] - max(lmax, rmax)

    print(f"#{t} {ans}")


for i in range(1, 11):
    n = int(input())
    bullis = list(map(int, input().split()))
    count = 0
    for b in range(2, n-1):
        if bullis[b] <= bullis[b-1] or bullis[b] <= bullis[b+1]:
            continue
        elif bullis[b] <= bullis[b-2] or bullis[b] <= bullis[b+2]:
            continue
        else:
            count += bullis[b]-max(bullis[b-1], bullis[b-2],
                                   bullis[b+1], bullis[b+2])
    print(f"#{i} {count}")
