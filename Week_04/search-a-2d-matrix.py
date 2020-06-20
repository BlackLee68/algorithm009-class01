# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  示例 1:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
#  示例 2:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # define a binary search function
    # the input array is one dimension
    def binarySearch(self, array, target) -> bool:
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            if target < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # same as binary search
        if not matrix or not matrix[0]: return False
        m,n = len(matrix), len(matrix[0])
        mid = 0
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[mid][0] or target == matrix[mid][n-1]:
                return True
            if matrix[mid][0] < target < matrix[mid][n-1]:
                break
            # update left and right
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][n-1]:
                left = mid + 1
        # apply binary search
        print(mid)
        print(matrix[mid])
        return self.binarySearch(matrix[mid], target)
# leetcode submit region end(Prohibit modification and deletion)
