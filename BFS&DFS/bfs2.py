from collections import deque

# 4, 5
rows, cols = map(int, input().split())
grid = []

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(rows):
    grid.append(list(map(int, input().split())))

def bfs(graph, start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    graph[start_x][start_y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = 3

def start(graph):
    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1:
                visited[i][j] = True


    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 2 and not visited[i][j]:
                bfs(graph, i, j, visited)


start(grid)

count = sum(cell == 3 for row in grid for cell in row)
print(count)




    



