from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    q = deque([(characterX,characterY)])

    for i in rectangle:



    while q:
        cx, cy = q.popleft()

        if cx == itemX and cy == itemY:
            return
        
        for dx, dy in (1,0),(0,1), (-1,0), (0,-1):
            if True:


    return