target = list(map(int, input().split()))
nums_len = len(target)

result = []
visited = [False for _ in range(nums_len)]

def backtracking(start, current):
    result.append(current[:])
    
    for i in range(start, nums_len):
        current.append(target[i])   # 선택
        backtracking(i + 1, current)  # 다음 인덱스부터 재귀
        current.pop()                 # 선택 취소 (백트래킹)

backtracking(0, [])
print(result)