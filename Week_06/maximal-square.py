"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 重复子问题-》这个题目的重复子问题不好想，是用每个点作为正方形的右下角来
        # 进行状态的递推，如果一个正方形为一个大正方形，则可以整个正方形进行递推
        # 又下角的值，一直到整个正方形的最右下角位置
        # 状态定义-》定义一个和matrix相同的二维矩阵来存储状态
        # DP方程-》res[i][j] = min(res[i-1][j],res[i][j-1],res[i-1][j-1]) + 1
        #   注意一些边界条件
        # 也可以直接原址进行，减少空间复杂度
        # using new space
        if not matrix: return 0
        max_length = 0
        row = len(matrix)
        clo = len(matrix[0])
        res = [[0]*clo for _ in range(row)]
        for i in range(row):
            for j in range(clo):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        res[i][j] = 1
                        if max_length < res[i][j]:
                            max_length = res[i][j]
                        continue
                    res[i][j] = min(res[i-1][j],res[i][j-1],res[i-1][j-1]) + 1
                    if res[i][j] > max_length:
                        max_length = res[i][j]
        return max_length * max_length
        # 这道题还可以采用暴力法，从左上角到右下角一个一个找下去，中间维护一个最大的正方形
        # violence