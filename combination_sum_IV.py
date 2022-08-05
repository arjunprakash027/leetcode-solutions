class Solution(object):
    def combinationSum4(self, N, T):
        dp = [0] * (T + 1)
        dp[0] = 1
        for i in range(1, T+1):
            for num in N:
                if num <= i: dp[i] += dp[i-num]
        return dp[T]
