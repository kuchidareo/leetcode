class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        summation = 0

        for right in range(len(nums)):
            summation += nums[right]
            
            if summation >= target:
                while summation >= target:
                    summation -= nums[left]
                    ans = min(ans, right+1 - left)
                    left += 1





        if ans != float('inf'):
            return ans
        else:
            return 0
                


            
