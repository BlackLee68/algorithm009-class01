# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
#
#
#  每次转换只能改变一个字母。
#  转换过程中的中间单词必须是字典中的单词。
#
#
#  说明:
#
#
#  如果不存在这样的转换序列，返回 0。
#  所有单词具有相同的长度。
#  所有单词只由小写字母组成。
#  字典中不存在重复的单词。
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
#  示例 1:
#
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#
#
#  示例 2:
#
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from collections import defaultdict


class Solution:
    # def judgeFuc(self, str1, str2) -> bool:
    #     # len(str1) == len(str2)
    #     change = 0
    #     for i in range(len(str1)):
    #         if str1[i] != str2[i]:
    #             change += 1
    #     return change == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # same as the geuin, using bfs
        if not beginWord or not endWord or not wordList:
            return 0
        # wtf-> to reduce the time of searching right value in
        # wordList
        helpDict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                helpDict[word[:i] + "*" + word[i + 1:]].append(word)

        visited = set()
        que = deque()
        que.append((beginWord, 1))
        # 0 means the level
        while que:
            cur, steps = que.popleft()
            visited.add(cur)
            for i in range(len(cur)):
                midStatus = cur[:i] + "*" + cur[i + 1:]
                # judge using dict
                for word in helpDict[midStatus]:
                    if word == endWord:
                        return steps + 1
                    if word not in visited:
                        que.append((word, steps + 1))
                # 提前减枝，不然还会运行到判断是否在visited那里
                helpDict[midStatus] = []
        return 0

# leetcode submit region end(Prohibit modification and deletion)
