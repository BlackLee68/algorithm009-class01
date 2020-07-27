"""

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 使用动态规划的思想，主要是状态的定义
        # 这里题目中求解最大或者最小，存在最优子结构问题
        # 新加入的一个数字需要和前面的所有状态进行联系和计算
        # 状态之间的转化需要进行一些条件的判断
        # 状态转移方程包含max或者min，可能和上一个状态或者以前的
        # 所有状态有关
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                for j in range(i):
                    if nums[i] > nums[j] and (dp[j] + 1) > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)