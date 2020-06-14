# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        # solution: 1, baoli  2,hash table
        # 1, baoli, 使用了O（nlogn）时间复杂度和O（n）space
        # s = sorted(s)
        # t = sorted(t)
        # return s == t

        # using hash table->O(n) space and O(n) time
        if len(s) != len(t): return False
        dit = {}
        for item1 in s:
            if item1 in dit:
                dit[item1] += 1
            else:
                dit[item1] = 1
        for item2 in t:
            if item2 not in dit:
                return False
            else:
                dit[item2] -= 1
        for _, value in dit.items():
            if value != 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
