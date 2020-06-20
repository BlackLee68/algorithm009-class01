# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换
# 需遵循如下规则：
#
#
#  每次转换只能改变一个字母。
#  转换后得到的单词必须是字典中的单词。
#
#
#  说明:
#
#
#  如果不存在这样的转换序列，返回一个空列表。
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
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
#
#
#  示例 2:
#
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
#  Related Topics 广度优先搜索 数组 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque, defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 所有的最短转换序列都在同一层
        # using bfs, using deque
        if endWord not in wordList or not wordList:
            return []
        res = []
        que = deque()
        target_level = 0
        # make dict for worlist
        wordDcit = defaultdict(list)
        length = len(beginWord)
        for word in wordList:
            for i in range(length):
                wordDcit[word[:i]+"*"+word[i+1:]].append(word)
        # bfs
        visited = set()
        que.append([beginWord,0,[beginWord]]) # 0 means level, [] means path
        while que:
            #print(visited)
            cur, level, path = que.popleft()
            visited.add(cur)
            for i in range(length):
                mid_cur = cur[:i]+"*"+cur[i+1:]
                for word in wordDcit[mid_cur]:
                    # matching pattern
                    if word == endWord and target_level==0:
                        res.append(path+[word])
                        target_level = level+1
                        continue
                    elif word == endWord and level+1==target_level:
                        res.append(path+[word])
                        continue
                    if word not in visited:
                        que.append([word, level+1, path+[word]])
                #wordDcit[mid_cur] = []
        # get resut
        return res
# leetcode submit region end(Prohibit modification and deletion)
