"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 暴力法，求每种分割情况下，所能得到的所有子数组和最大值
        # 然后从最大值中取最小值
        # 暴力的方法很难写出来--
        # 使用动态规划
        # 1，重复子问题-》从m去下手开进行状态递推感觉比较好，从分成一个到分成m个
        # 2，状态定义-》res[i]代表分成i个飞空连续子数组时最后的最小最大值
        # 3，DP方程-》res[1] = sum(nums)
        #            我还需要记录一下上一个状态和最大的子数组的序列[m:n]
        #            下一个状态在上一个状态和最大的那个子数组里面去分
        #            res[i]     res[i-1]
        left, right = max(nums),sum(nums)
        while left < right:
            mid = (left + right) // 2
            sums, cnt = 0, 1
            # 这里计算以mid为目标和，可以分出多少组
            for i in nums:
                if sums + i > mid:
                    cnt += 1
                    sums = i
                else:
                    sums += i
            if cnt <= m:
                right = mid
            else:
                left = mid + 1
        return left