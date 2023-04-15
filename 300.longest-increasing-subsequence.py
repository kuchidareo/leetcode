class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            i_max = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    i_max = max(i_max, dp[j] + 1)
            dp[i] = i_max

        return max(dp)

