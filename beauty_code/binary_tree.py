"""
这里给出二叉树节点的定义，类似于链表的定义，只不过二叉树
包含两个后继节点
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
这里给出二叉树的三种遍历的标准递归写法，因为在二叉树这种数据结构中，含有重复的局部二叉子树，采用递归可以方便的
对整个树进行相关元素的操作
先序遍历：根左右
中序遍历：左根右
后序遍历：左右根
"""


# 先序遍历
def pre_order(self, root):
    if root:
        self.traver_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)


# 中序遍历
def in_order(self, root):
    if root:
        self.inorder(root.left)
        self.traver_path.append(root.val)
        self.inorder(root.right)


# 后序遍历
def post_order(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traver_path.append(root.val)
