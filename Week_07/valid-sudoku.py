"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判断三个条件是否符合
        # 需要一个处理，从index到3X3块儿的处理
        # input-》（i，j）： （i//3）*3+ (j//3)
        row_length = len(board)
        clo_length = len(board[0])
        # 先将每个条件的数组搞出来
        row = defaultdict(list)
        clo = defaultdict(list)
        area = defaultdict(list)
        for i in range(row_length):
            for j in range(clo_length):
                if board[i][j] == ".":
                    continue
                row[i].append(board[i][j])
                clo[j].append(board[i][j])
                area[(i//3)*3+(j//3)].append(board[i][j])
        # judge
        for i in range(row_length):
            for j in range(clo_length):
                if board[i][j]==".": continue
                # judge row
                if sum(1 for item in row[i] if board[i][j]==item) > 1: return False
                # clo
                if sum(1 for item in clo[j] if board[i][j]==item) > 1: return False
                # area
                if sum(1 for item in area[(i//3)*3+(j//3)] if board[i][j]==item) > 1: return False
        return True