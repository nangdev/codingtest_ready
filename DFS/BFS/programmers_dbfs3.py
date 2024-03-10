from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])

    v = [[0]*M for _ in range(N)]

    q = deque([(0, 0)])

    v[0][0] = 1

    while q:
        cx, cy = q.popleft()

        if cx == N-1 and cy == M-1:
            return v[cx][cy]

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = cx+dx, cy+dy

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1

    return -1
