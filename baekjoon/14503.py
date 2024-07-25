# import sys
# sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
cx, cy, d = map(int, input().split())

# d 0 북 1 동 2 남 3 서

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
back = [[1, 0], [0, -1], [-1, 0], [0, 1]]   # 남서북동

while True:
    if arr[cx][cy] == 0:  # 1번 조건
        arr[cx][cy] = -1
        cnt += 1

    chk = True  # 주변칸 확인
    for dx, dy in direc:
        nx, ny = cx+dx, cy+dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                chk = False
                break

    if chk:  # 2번 조건
        nx, ny = cx + back[d][0], cy + back[d][1]
        if 0 <= nx < n and 0 <= ny < m and (arr[nx][ny] == 0 or arr[nx][ny] == -1):
            cx, cy = nx, ny
            continue
        elif 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            break

    else:  # 3번 조건
        d -= 1
        if d == -1:
            d = 3

        nx, ny = cx + direc[d][0], cy + direc[d][1]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            cx, cy = nx, ny


print(cnt)