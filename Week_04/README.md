# 学习笔记

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
这个问题类似于寻找旋转数组中的最小值，在一个半有序数组中（确实存在反转点），
无序的地方就是数组翻转的地方，就是半有序数组中的最小值所在的地方，最小值
所在的地方有一些特定的性质，它的左右两边都是有序数组，可以利用这个性质来找
到这个最小值点，基于二分查找加速找到极小值点的过程，整体思路是不停二分查找
无序的那一半，知道达到跳出条件，也即是左右均为有序数组。

示例代码如下：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums) < 3: return min(nums)
        if nums[0] < nums[-1]: return nums[0]
        left, right = 0, len(nums) - 1
        mid = 0
        min_num = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[mid+1] <= nums[right]:
                return mid+1
            if nums[left] <= nums[mid-1] and nums[mid] <= nums[right]:
                return mid
            # update left and right
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1
```

ps:天津转战长春终于出差归来