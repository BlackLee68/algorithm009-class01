# 设计实现双端队列。
# 你的实现需要支持以下操作：
#
#
#  MyCircularDeque(k)：构造函数,双端队列的大小为k。
#  insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
#  insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
#  deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
#  deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
#  getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
#  getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
#  isEmpty()：检查双端队列是否为空。
#  isFull()：检查双端队列是否满了。
#
#
#  示例：
#
#  MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
# circularDeque.insertLast(1);			        // 返回 true
# circularDeque.insertLast(2);			        // 返回 true
# circularDeque.insertFront(3);			        // 返回 true
# circularDeque.insertFront(4);			        // 已经满了，返回 false
# circularDeque.getRear();  				// 返回 2
# circularDeque.isFull();				        // 返回 true
# circularDeque.deleteLast();			        // 返回 true
# circularDeque.insertFront(4);			        // 返回 true
# circularDeque.getFront();				// 返回 4
#  
#
#
#
#  提示：
#
#
#  所有值的范围为 [1, 1000]
#  操作次数的范围为 [1, 1000]
#  请不要使用内置的双端队列库。
#
#  Related Topics 设计 队列

#
# leetcode submit region begin(Prohibit modification and deletion)
# 采用两种写法->使用列表   使用双向链表
# 使用列表
class MyCircularDeque:
    # two ways to realize the deque
    # 1: using list
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._deque = []
        self._target = k
        self._capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self._capacity == 0:
            return False
        else:
            self._deque = [value] + self._deque
            self._capacity -= 1
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self._capacity == 0:
            return False
        else:
            self._deque.append(value)
            self._capacity -= 1
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self._capacity == self._target:
            return False
        else:
            self._deque = self._deque[1:]
            self._capacity += 1
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self._capacity == self._target:
            return False
        else:
            self._deque.pop()
            self._capacity += 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self._capacity == self._target:
            return -1
        else:
            return self._deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self._capacity == self._target:
            return -1
        else:
            return self._deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._capacity == self._target

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._capacity == 0


# 使用链表
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyCircularDeque:
    # two ways to realize the deque
    # 1: using list
    # 2: using linkedlist(with tail pointer linkedlist)

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._deque_head = Node(0)
        self._deque_tail = Node(-1)
        self._deque_head.next = self._deque_tail
        self._deque_tail.pre = self._deque_head
        self._capacity = k
        self._target = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self._capacity == 0:
            return False
        else:
            # 这里有两种情况，初始情况和一般情况\
            temp_node = Node(value)
            if self._capacity == self._target:
                temp_node.next = self._deque_tail
                temp_node.pre = self._deque_head
                self._deque_head.next = temp_node
                self._deque_tail.pre = temp_node
            else:
                temp_node.next = self._deque_head.next
                temp_node.pre = self._deque_head
                self._deque_head.next.pre = temp_node
                self._deque_head.next = temp_node
            self._capacity -= 1
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self._capacity == 0:
            return False
        else:
            # 也是两种情况
            temp_node = Node(value)
            if self._capacity == self._target:
                temp_node.next = self._deque_tail
                temp_node.pre = self._deque_head
                self._deque_head.next = temp_node
                self._deque_tail.pre = temp_node
            else:
                temp_node.next = self._deque_tail
                temp_node.pre = self._deque_tail.pre
                self._deque_tail.pre.next = temp_node
                self._deque_tail.pre = temp_node
            self._capacity -= 1
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self._capacity == self._target:
            return False
        else:
            self._deque_head.next.next.pre = self._deque_head
            self._deque_head.next = self._deque_head.next.next
            self._capacity += 1
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self._capacity == self._target:
            return False
        else:
            self._deque_tail.pre.pre.next = self._deque_tail
            self._deque_tail.pre = self._deque_tail.pre.pre
            self._capacity += 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self._capacity == self._target:
            return -1
        else:
            return self._deque_head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self._capacity == self._target:
            return -1
        else:
            return self._deque_tail.pre.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._capacity == self._target

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._capacity == 0

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
