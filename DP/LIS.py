"""
문제: 최장 증가 부분수열 (LIS, Longest Increasing Subsequence)

정수 배열이 주어질 때, 증가하는 부분수열 중 가장 긴 것의 길이를 구하세요. 
여기서 "부분수열"은 연속일 필요는 없고, 순서만 유지하면 중간을 건너뛰어도 돼요.

입력: nums = [10, 9, 2, 5, 3, 7, 101, 18]
출력: 4
설명: [2, 3, 7, 101] 또는 [2, 3, 7, 18] 등이 길이 4로 최장
"""
nums = list(map(int, input().split()))

dp = [0] * len(nums)
dp[0] = 1

def length_of_lis(nums: list[int]) -> int:
    for i in range(1, len(nums)):
        dp[i] = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

length_of_lis(nums)
print(max(dp))