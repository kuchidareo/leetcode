class Solution:
    def rob(self, nums: List[int]) -> int:
        buf = [0, 0]
        for n in nums:
            tar = buf[1] + n
            if tar > buf[0]:
                buf[1] = buf[0]
                buf[0] = tar
            else:
                buf[1]  = buf[0]
        return max(buf)


