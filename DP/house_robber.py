# 문제: 집 도둑 (House Robber)
# 도둑이 일렬로 늘어선 집들을 털려고 합니다. 각 집에는 돈이 들어있는데, 
# 바로 옆집을 연달아 털면 경보가 울려요. (한 칸 띄엄띄엄은 괜찮아요.) 훔칠 수 있는 최대 금액을 구하세요.

"""
입력: money = [1, 2, 3, 1]
출력: 4
설명: 1번째 집(2) + 4번째 집(1)? 아니고
     1번째 집(1) + 3번째 집(3) = 4가 최대
     (2번째와 4번째를 털면 2+1=3, 그보다 1+3=4가 더 큼)
"""

money = list(map(int, input().split()))

dp = [0] * len(money)
dp[0] = money[0]
dp[1] = max(dp[0], money[1])

def house_robber(nums):
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

house_robber(money)
print(max(dp))