from collections import deque

rows, cols = map(int, input().split())
grid = []

for _ in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(graph, start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    count = 1

    while queue:
        node = queue.popleft()
        for i in range(4):
            nx, ny = node[0] + dx[i], node[1] + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and graph[nx][ny] == 1 and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                queue.append([nx, ny])
    return count


def start(graph):
    visited = [[False] * cols for i in range(rows)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1 and not visited[i][j]:
                count = max(count, bfs(graph, i, j, visited))
    
    print(count)

start(grid)
            


    

        
            