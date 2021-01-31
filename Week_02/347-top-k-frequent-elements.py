class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 尚未参考题解
        # 使用字典存下各个数字出现频率
        x = {}
        for i in range(len(nums)):
            if nums[i] not in x:
                x[nums[i]] = 1
            else:
                x[nums[i]] += 1
        # 对字典依据value排序
        res = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse = True)}
        # 返回前K的key
        return list(res)[:k]