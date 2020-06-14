# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#  示例：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # using dummy for convince
        if not l1: return l2
        if not l2: return l1 # make sure l1 and l2 are not empty
        dummy = ListNode(0)
        p = dummy
        v1 = v2 = 0
        while l1 or l2:
            v1 = l1.val if l1 else l2.val + 1
            v2 = l2.val if l2 else l1.val + 1
            if v1 < v2:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
