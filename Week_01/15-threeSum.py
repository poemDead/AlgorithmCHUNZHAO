'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
链接：https://leetcode-cn.com/problems/3sum
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先进行排序，方便之后的双指针左右夹逼
        nums.sort() 
        res = []
        for i in range(len(nums)-2):
            # 如果第一个数就大于零就不用试了，肯定不存在
            if nums[i] > 0: break 
            # 从第二个数开始，如果和上一个相同，那结果肯定会重复，就不用试了
            if i > 0 and nums[i] == nums[i-1]: continue 
            # 双指针开始
            j, k = i + 1, len(nums)-1 # 
            while j < k:
                # 判定三数之和是否为零
                t = nums[i] + nums[j] + nums[k]
                # 如果大于零，说明需要缩小一下，鉴于数组有序排列，那肯定是减少最大的
                if t > 0: k-=1
                # 同理，如果小于零，说明需要扩大一下，那肯定是增加最小的
                if t < 0: j+=1
                # 等于零则输出结果
                if t == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # 此处先判定while很重要，后判定会将一些情况错误跳过
                    while j < k and nums[j] == nums[j+1]: j+=1
                    while j < k and nums[k] == nums[k-1]: k-=1
                    j+=1
                    k-=1
        return res