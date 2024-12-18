"""
Problem: Permutations
Generate all permutations of a list.
"""

def permute(nums):
    res = []
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for num in nums:
            if num not in path:
                backtrack(path + [num])
    backtrack([])
    return res

nums = [1, 2, 3]
print("Permutations:", permute(nums))
