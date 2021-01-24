'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

链接：https://leetcode-cn.com/problems/merge-sorted-array
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 三指针，从后向前
        if m == 0 :
            nums1[:] = nums2
        if n != 0:
            i, j, k = m-1, n-1, m+n-1
            while i>=0 and j>=0:
                if nums1[i] <= nums2[j]:
                    nums1[k] = nums2[j]
                    j-=1
                    k-=1
                else:
                    nums1[k] = nums1[i]
                    i-=1
                    k-=1
                if j>=0: nums1[k-j:k+1] = nums2[:j+1]

        # # 1. 暴力
        # if n != 0:
        #     for i in range(1,n+1):
        #         nums1[-i] = nums2[-i]
        #     nums1.sort()