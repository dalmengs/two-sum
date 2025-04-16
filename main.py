from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


# nums = [3, 2, 4]
# target = 6
# print(twoSum(nums, target)) # expected output: [1, 2]

# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target)) # expected output: [0, 1]

# nums = [3, 3]
# target = 6
# print(twoSum(nums, target)) # expected output: [0, 1]

