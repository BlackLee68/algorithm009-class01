# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  你可以假设数组中不存在重复元素。
#
#  示例 1:
#
#  输入: [3,4,5,1,2]
# 输出: 1
#
#  示例 2:
#
#  输入: [4,5,6,7,0,1,2]
# 输出: 0
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # violence
        # but! min() function should not be included
        # return min(nums)
        # 转化为寻找翻转点，反转点有什么特性，就是左右两边
        # 分出来的数组都是升序的，有可能需要左移一位或者
        # 右移一位, 并且不满足nums[0]<nums[-1], 也即是
        # 不存在翻转情况
        if not nums: return -1
        if len(nums) < 3: return min(nums)
        if nums[0] < nums[-1]: return nums[0]
        left, right = 0, len(nums) - 1
        mid = 0
        min_num = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid+1] <= nums[right]:
                return nums[mid+1]
            if nums[left] <= nums[mid-1] and nums[mid] <= nums[right]:
                return nums[mid]
            # update left and right
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1
# leetcode submit region end(Prohibit modification and deletion)
