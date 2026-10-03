nums = list(map(int, input().split()))
nums_len = len(nums)

visited = [False for _ in range(nums_len)]
current = []      # 현재 순열
answer = []       # 결과 모음

def back():
    if len(current) == nums_len:
        answer.append(current[:])   # 복사해서 저장
        return

    for i in range(nums_len):   # 항상 0부터
        if visited[i]:
            continue

        visited[i] = True
        current.append(nums[i])

        back()

        visited[i] = False
        current.pop()

back()
print(answer)