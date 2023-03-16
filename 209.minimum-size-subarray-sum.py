class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        stack = [0]
        can = []
        
        while stack:
            left = stack.pop()
            summation = nums[left]
            
            right = left
            while summation <= target and right < len(nums)-1:
                right += 1
                summation += nums[right]
            
            left = left -1
            while summation >= target:
                left += 1
                summation -= nums[left]

            can.append(right - (left - 1) + 1)
            
            if right+1 < len(nums):
                stack.append(right+1)

        return min(can) if can != [] else 0



            

            
