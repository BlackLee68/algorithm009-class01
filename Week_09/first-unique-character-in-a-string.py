"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # using dict to solve
        if not s: return -1
        dit = OrderedDict()
        for item in s:
            if item not in dit:
                dit[item] = 1
            else:
                dit[item] += 1
        for index, item in enumerate(s):
            if dit[item] == 1:
                return index
        return -1