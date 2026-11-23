class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_value = cureent_sum = sum(nums[:k])
        for i in range(len(nums)-k):
            cureent_sum = cureent_sum - nums[i] + nums[i+k]
            max_value = max(max_value,cureent_sum)
        return max_value / k