# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
#  示例:
#
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # first solution
        # if k == 0:
        #     return [[]]
        # return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        # second solution
        return list(combinations(range(1, n+1), k))
