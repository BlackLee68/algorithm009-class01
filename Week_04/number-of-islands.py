# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dfs(self, grid, i, j, visited):
        # every recursion, the grid have to change
        # 注意这里有较多的退出条件
        # 本质上还是构造一个递归树，每个点都有四个后继节点，然后在
        # 每个后记节点上再继续进行判断和递归
        if (i,j) in visited:
            return
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return
        if grid[i][j]  == "0":
            return
        visited.add((i,j))
        grid[i][j] = "0"
        # 这里注意不包含斜线方向
        for move_i, move_j in [(-1,0),(1,0),(0,-1),(0,1)]:
            self.dfs(grid, i + move_i, j + move_j, visited)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0":
                    continue
                else:
                    num += 1
                    self.dfs(grid, i, j, visited)
        return num
# leetcode submit region end(Prohibit modification and deletion)
