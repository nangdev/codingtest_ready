from collections import deque

N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 도로 정보 입력 받기
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([X])
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for n_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[n_node] == -1:

            #최단 거리 갱신
            distance[n_node] = distance[now] + 1
            q.append(n_node)

#최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)

