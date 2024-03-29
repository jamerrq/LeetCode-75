from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[-1] = cost[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = cost[i]
            if i != n - 2:
                dp[i] += min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])
