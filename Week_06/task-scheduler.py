"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/task-scheduler
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 动态规划
        #　１，重复子问题　
        # 2,状态定义
        # 3，DP方程
        # 先不用动态规划来解决，使用一种数学思想，整个的时间由最大任务次数的任务来解决，
        #　得到最大任务次数的任务后，将他们均匀排任务，然后将其他任务依次插入每两个最大
        # 任务次数的任务之间
        if len(tasks) == 1 or n==0: return len(tasks)
        max_num = 0
        max_num_num = 0
        dit = {}
        for item in tasks:
            if item not in dit:
                dit[item] = 1
            else:
                dit[item] += 1
            if dit[item] > max_num:
                max_num = dit[item]
        for key, value in dit.items():
            if value == max_num:
                max_num_num += 1
        res = (max_num-1)*(n+1) + max_num_num
        return res if res > len(tasks) else len(tasks)