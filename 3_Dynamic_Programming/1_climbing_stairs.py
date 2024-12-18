"""
Problem: Climbing Stairs
Calculate distinct ways to climb n stairs.
"""

def climb_stairs(n):
    if n <= 2: return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 5
print("Ways to climb stairs:", climb_stairs(n))
