"""
一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。

给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

请注意：

石子的数量 ≥ 2 且 < 1100；
每一个石子的位置序号都是一个非负整数，且其 < 231；
第一个石子的位置永远是0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frog-jump
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 可以使用暴力法，用递归的思想，每步都选择最多三种跳的方法
        # 递归树往下递归，如果所有的路线都不能跳到最后一个格子，那么
        # 就代表不能不能过河，只要有一个路径可以到达最后一个格子，就代表
        # 可以过河，但时间复杂度是指数级的==
        # 后续补充这种方法
        # 先采用动态规划来求解
        # 三个主要问题：
        # 1，重复子问题-》假设上一个状态能够跳到，
        # 2，状态定义
        # 3，DP方程
        # 利用哈希表来存储每个石头的状态
        dit = defaultdict(set)
        # base case
        for stone in stones:
            dit[stone]
        dit[stones[0]].add(0)
        for item in stones:
            for base_jump in dit[item]:
                for new_jump in [base_jump-1, base_jump, base_jump+1]:
                    if new_jump < 1: # 这里改为必须大于等于1，防止出现对其本身的修改，防止出现set changed during iteration 错误
                        continue
                    if item + new_jump in dit:
                        dit[item+new_jump].add(new_jump)
        return True if len(dit[stones[-1]]) > 0 else False