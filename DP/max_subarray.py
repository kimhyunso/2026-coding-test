# 입력: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 출력: 6
# 설명: [4, -1, 2, 1] 의 합이 6으로 최대

nums = list(map(int, input().split()))

dp = [0] * len(nums)
dp[0] = nums[0]
dp[1] = max(nums[1], dp[0] + nums[1])

def max_subarray(nums):
    for i in range(2, len(nums)):
        dp[i] = max(nums[i], dp[i -1] + nums[i])


max_subarray(nums)
print(max(dp))