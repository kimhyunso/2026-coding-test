nums = [2, 5, 10, 9, 8, 6, 3]
nums.sort()

def binary_search(find_value):
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle_pivot = (start + end) // 2
        search_value = nums[middle_pivot]

        if find_value == search_value:
            return middle_pivot
        elif find_value < search_value:
            end = middle_pivot - 1
        elif find_value > search_value:
            start = middle_pivot + 1

    return -1

result = binary_search(3)
print(result)









