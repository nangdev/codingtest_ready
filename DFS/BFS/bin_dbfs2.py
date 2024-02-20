from collections import deque


def dfs(x, y, cur):
    global res

    if x == N-1 and y == M-1:
        res = min(res, cur)
        return

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx = x+dx
        ny = y+dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and v[nx][ny] == 0:
            v[nx][ny] = 1
            dfs(nx, ny, cur+1)


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return arr[x][y]


        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx,ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
    
    # 도달하지 못할 경우
    return 0


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

v = [[0]*M for i in range(N)]
v[0][0] = 1

res = 9999
dfs(0, 0, 1)


print(bfs(0, 0))
print(res)
