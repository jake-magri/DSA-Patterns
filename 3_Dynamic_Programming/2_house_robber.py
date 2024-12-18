"""
Problem: House Robber
Find max sum by robbing non-adjacent houses.
"""

def rob(nums):
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr

houses = [2, 7, 9, 3, 1]
print("Max money robbed:", rob(houses))
