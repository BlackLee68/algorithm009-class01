class Solution:
    # using reverse function
    def reverse(self, nums: List[int], start, end) -> None:
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k % len(nums) == 0: return None
        '''
        # 第一种方法：暴力法，但会超出时间限制
        move_step = k % len(nums)
        for _ in range(move_step):
            pop_value = nums[-1]
            i = len(nums) - 2
            while i >= 0:
                nums[i+1] = nums[i]
                i -= 1
            nums[0] = pop_value
        '''
        '''
        # 第二种方法：采用数组切片操作，这里不确定空间复杂度是否为O(1)
        move_step = k % len(nums)
        nums[:move_step+1], nums[move_step:] = nums[-move_step:], nums[:-move_step]
        '''
        # 第三种方法，采用翻转数组
        move_step = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, move_step - 1)
        self.reverse(nums, move_step, len(nums) - 1)