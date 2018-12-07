
# trick: dp[i] stores the subseq end with element i (must end with element i!!!)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
        return max(dp)
        
