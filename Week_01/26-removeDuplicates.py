'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针的思路
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1