"""
문제: 랜선 자르기

길이가 제각각인 랜선 K개가 있습니다. 이 랜선들을 잘라서 같은 길이의 랜선 N개 이상을 만들려고 합니다. 만들 수 있는 랜선 한 개의 최대 길이를 반환하세요.

자르기만 가능하고 이어 붙일 수 없음
자르고 남은 자투리는 버림
길이는 정수(cm)
"""

cables = list(map(int, input().split()))
need = int(input()) # 필요한 랜선 수

def max_length(cables, need):
    start = 1
    end = max(cables) # 가장 긴 랜선
    answer = 0

    while start <= end:
        L = (start + end) // 2 # 이번에 시도해 볼 길이 (후보)

        count = 0
        for cable in cables: # 길이 L로 잘랐을 때 나오는 랜선 개수 세기
            count += cable // L

        if count >= need: # 필요한 랜선보다 많거나 같을 경우
            answer = L
            start = L + 1
        else: # 필요한 랜선보다 적을 경우
            end = L - 1
    return answer

result = max_length(cables, need)
print(result)
