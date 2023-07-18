#OK

from collections import deque

n, m, v = map(int, input().split()) # n: 정점의 개수 / m: 간선의 개수 / v: 시작 정점 번호
graph = [[False] * (n+1) for _ in range(n+1)] # 초기값 False인 함수 설정

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True #방문 처리
    print(v, end=" ") #방문 표시
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i] == 1: #방문기록이 없고 인덱스에 값이 있다면
            dfs(i) #방문한다. 재귀함수 활용
            #호출될 때마다 visited 1 되고 재귀되어 v에 i가 들어간다.

def bfs(v):
    q = deque([v]) #방문한 것을 순서대로 넣을 큐
    visited_bfs[v] = True # 방문처리
    while q: #q안에 데이터가 없어질때까지 실행
        v = q.popleft() #q 맨 앞에 있는 값을 꺼내서 출력한다.(q.pop대신 q.popleft를 사용한 이유는 시간복잡도가 낮기 때문이다)
        print(v, end = " ")
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i] == 1: #방문 기록이 없고 인덱스에 값이 있다면(연결되어 있다면)
                q.append(i) #큐에 추가
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)








