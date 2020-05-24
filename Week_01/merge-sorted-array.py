# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明:
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例:
#
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(nlog(n)) time O(1) space
        if not nums2: return None
        '''
        # 第一种方法：赋值后直接排序
        nums1[m:] = nums2
        nums1.sort()
        # 有一个疑问是进行切片赋值的过程中，有没有过多内存的消耗？
        '''
        # 第二种方法，使用三指针法
        i = m - 1 # nums1 pointer
        j = n - 1 # nums2 pointer
        k = m + n - 1 # right value place
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        nums1[:j + 1] = nums2[:j + 1]
# leetcode submit region end(Prohibit modification and deletion)
