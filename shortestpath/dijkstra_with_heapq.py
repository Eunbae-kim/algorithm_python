import heapq
import sys
input = sys.stdin.readline()
INF = int(1e9) #무한을 의미하는 갑승로 10억 설정

# 별도 visited 방문처리 테이블 만들 필요 없고
# 가장 짧은 거리 구하는 함수도 필요 없음

#노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split())

# 시작 노드 번호 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] *(n+1)

# 모든 간선 정보를 입력 받기
for _ in range(n):
    a,b,c = map(int, input.split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q=[]

    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하며 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

