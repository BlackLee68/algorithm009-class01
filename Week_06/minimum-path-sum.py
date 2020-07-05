""""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""
import numpy as np
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 类似于机器人地图，机器人是求一共有多少路径，这里求总和最少的
        # 路径
        # 使用动态规划
        # 1，重复子问题-》从右下角开始往回找，上一步是选择向上或者向左最小的一步
        # 2，状态定义-》使用原始grid就可以，在更新状态的时候只需要更新index即可
        # 3，DP方程-》if grid[i-1][j] < grid[i][j-1]:
        #               i = i-1
        #            else:
        #               j = j-1
        # 有两个特殊边界-》左边界和上边界
        # 适应上述方法不AC，依旧使用向机器人一样的DP方程
        if not grid: return -1
        m,n = len(grid), len(grid[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j == n-1:
                    continue
                if i==m-1:
                    grid[i][j] += grid[i][j+1]
                elif j==n-1:
                    grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
        # 注意这题使用贪心法不可以，注意动态规划是每个状态都会找到最优解，然后一步步递推到最终的状态，动态规划中的随意一个状态都可以拿出来当做最后状态。