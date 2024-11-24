"""
LeetCode Questions
70 - Climbing stairs
322 - Coin change
1143 - Longest common subsequence
300 - Longest increasing subsequence
72 - Edit distance
"""

"""
Top-down recursive Fibonacci without memoization.
Time: O(2^N) | Space: O(N)
"""

def fib_top_down(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_top_down(n-1) + fib_top_down(n-2)


"""
Top-down recursive Fibonacci with memoization.
Time: O(N) | Space: O(N)
"""

def fib_top_down_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_top_down_memo(n-1, memo) + fib_top_down_memo(n-2, memo)
    return memo[n]


"""
Bottom-up Fibonacci using an array.
Time: O(N) | Space: O(N)
"""

def fib_bottom_up_array(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


"""
Bottom-up Fibonacci using 2 variables.
Time: O(N) | Space: O(1)
"""

def fib_bottom_up(n):
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        fib = prev2 + prev1
        prev2 = prev1
        prev1 = fib

    return prev1