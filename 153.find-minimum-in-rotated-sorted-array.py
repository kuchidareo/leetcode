class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 3:
            n = len(nums)
            first = 0
            mid = n // 2
            if nums[first] < nums[mid]:
                del nums[1:mid]
            else:
                del nums[mid+1:n]
        return min(nums)   
