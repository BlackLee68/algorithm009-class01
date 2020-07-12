"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # 判断三个条件是否符合
    #     # 需要一个处理，从index到3X3块儿的处理
    #     # input-》（i，j）： （i//3）*3+ (j//3)
    #     row_length = len(board)
    #     clo_length = len(board[0])
    #     # 先将每个条件的数组搞出来
    #     row = defaultdict(list)
    #     clo = defaultdict(list)
    #     area = defaultdict(list)
    #     for i in range(row_length):
    #         for j in range(clo_length):
    #             if board[i][j] == ".":
    #                 continue
    #             row[i].append(board[i][j])
    #             clo[j].append(board[i][j])
    #             area[(i//3)*3+(j//3)].append(board[i][j])
    #     # judge
    #     for i in range(row_length):
    #         for j in range(clo_length):
    #             if board[i][j]==".": continue
    #             # judge row
    #             if sum(1 for item in row[i] if board[i][j]==item) > 1: return False
    #             # clo
    #             if sum(1 for item in clo[j] if board[i][j]==item) > 1: return False
    #             # area
    #             if sum(1 for item in area[(i//3)*3+(j//3)] if board[i][j]==item) > 1: return False
    #     return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 使用递归方法
    #     if not board: return
    #     self.dfs(board)
    # def dfs(self, board):
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == ".":
    #                 for item in range(1,10):
    #                     board[i][j] = str(item)
    #                     if self.isValidSudoku(board):
    #                         if self.dfs(board):
    #                             return True
    #                         else:
    #                             board[i][j] = "."
    #                     else:
    #                         board[i][j] = "."
    #                 return False
    #     return True
    # 但是上面的递归超出时间限制
        # 采用不在进行每步判断是否有效的递归方式
        if not board: return
        row = [set(range(1,10)) for _ in range(9)]
        clo = [set(range(1,10)) for _ in range(9)]
        area = [set(range(1,10)) for _ in range(9)]
        # change row , clo area first
        empty = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    row[i].remove(int(board[i][j]))
                    clo[j].remove(int(board[i][j]))
                    area[(i//3)*3+(j//3)].remove(int(board[i][j]))
                else:
                    empty.append((i,j))
        def backtrack(level):
            if level == len(empty):
                return True
            i, j = empty[level]
            d = (i//3)*3 + (j//3)
            for val in row[i] & clo[j] & area[d]:
                board[i][j] = str(val)
                row[i].remove(val)
                clo[j].remove(val)
                area[d].remove(val)
                if backtrack(level+1):
                    return True
                row[i].add(val)
                clo[j].add(val)
                area[d].add(val)
            return False
        backtrack(0)


