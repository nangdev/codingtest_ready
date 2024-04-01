from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 0

    p = deque(progresses)
    s = deque(speeds)

    while p:
        day += 1

        for i in range(len(s)):
            p[i] += s[i]

        cnt = 0
        while True:
            if p:
                if p[0] >= 100:
                    p.popleft()
                    s.popleft()
                    cnt += 1
                else:
                    break
            else:
                break

        if cnt >= 1:
            answer.append(cnt)

    return answer