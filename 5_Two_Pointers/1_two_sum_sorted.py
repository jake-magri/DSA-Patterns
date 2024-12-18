"""
Problem: Two Sum II
Find two numbers that sum to a target in a sorted array.
"""

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

numbers = [2, 7, 11, 15]
target = 9
print("Indices:", two_sum(numbers, target))
