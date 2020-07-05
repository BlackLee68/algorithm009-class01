"""
给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = [[1,0,1],[0,-2,3]], k = 2
输出: 2
解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # 这个题完全没有思路呢==
        # row_len = len(matrix)
        # column_len = len(matrix[0])
        # res = float("-inf")
        # for column_index_left in range(column_len):
        #     for column_index_right in range(column_index_left, column_len):
        #         curr = 0
        #         arr = [0]
        #         for row in range(0, row_len):
        #             curr = curr + sum(matrix[row][column_index_left:column_index_right + 1])
        #             pos = bisect.bisect_left(arr, curr - k)
        #             if pos < len(arr):
        #                 res = max(curr - arr[pos], res)
        #             bisect.insort(arr, curr)
        # return res
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res