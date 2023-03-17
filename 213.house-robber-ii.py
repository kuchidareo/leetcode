class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        ans = 0

        rotate_nums_list = [nums[1:], nums[2:] + [nums[0]]]
        for rotate_nums in rotate_nums_list:
            can_ans = [0 for _ in range(len(rotate_nums))]
            can_ans[0] = rotate_nums[0]
            can_ans[1] = max(rotate_nums[0], rotate_nums[1])

            for j in range(2, len(rotate_nums)):
                can_ans[j] = max(can_ans[j-2]+rotate_nums[j], can_ans[j-1])
            
            ans = max(can_ans[-1], ans)

        return ans 

