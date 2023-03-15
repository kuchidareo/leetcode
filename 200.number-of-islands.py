class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def convertAround(row, col):
            grid[row][col] = '0'
            next_search_list = [(row, col-1), (row, col+1), (row+1, col), (row-1, col)]
            for nrow, ncol in next_search_list:
                if nrow >= 0 and nrow <= len(grid)-1 and ncol >= 0 and ncol <= len(grid[0])-1:
                    if grid[nrow][ncol] == '1':
                        convertAround(nrow, ncol)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    convertAround(row, col)
                    ans += 1
        return ans
                    
  
