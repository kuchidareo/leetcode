class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k == 1:
            return 1 if n <= 2 else 0

        if n == 1:
            return k
        elif n == 2:
            return k**2
        elif n == 3:
            return k**3 - k
        
        ans = [0 for _ in range(n)]
        ans[0] = k
        ans[1] = k ** 2
        ans[2] = k ** 3 - k

        for i in range(3, n):
            ans[i] = (k-1)*((k-1)*ans[i-3]) + k*(ans[i-1]-(k-1)*ans[i-3])
        return ans[-1]
