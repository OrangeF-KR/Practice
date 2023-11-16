import sys
from collections import deque
input = sys.stdin.readline
# 풀이방식은 bfs 도출 방식
n, m = map(int, input().split())
graph = [] # graph[0][0] 기본값 설정 실제 위치는 1,1로 시작

for i in range(n):
    graph.append(list(map(int, input().rstrip())))  # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

dx = [-1, 1, 0, 0] # bfs 방식으로 '동 서 남 북'을 검사하여 1인 값을 검사한다. 값이 1이어야 이동가능.
dy = [0, 0, -1, 1]
'''
 만약 1이라면 그 전 값에 +1을 하여 이동할 때 지나야 하는 최소 칸 수를 더해준다.
 이렇게 쭉 검사 하다보면 마지막 graph[n - 1][m - 1]에는 최소 칸 수의 최종값이 들어가게 된다.
'''
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))
'''
소 칸 수의 최종값이 들어가게 된다.

초기 입력 값은 아래와 같지만,

4 6
101111
101010
101011
111011

1~3 과정을 수행하고 나면 graph 배열의 형태는 아래처럼 바뀐다.

[3,  0,  9, 10, 11, 12]
[2,  0,  8,  0,  12,  0]
[3,  0,  7,  0,  13, 14]
[4,  5,  6,  0,  14, 15]

참고로 소스코드 상에서 첫 번째 시작 위치가 다시 방문할 수 있도록 되어서 graph[0][0] 값이 3으로 바뀌었다.
그러나 이 문제에서는 단순히 가장 오른쪽 아래 위치로 이동하는 것을 요구하고 있기 때문에 답을 도출하는 데에는 문제가 없다.
'''