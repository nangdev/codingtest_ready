from collections import deque

p = deque([1,2,3])

a = p.popleft()
p.append(a)

p.popleft()

print(p)
