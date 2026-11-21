class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        if not nums:
            return []
        
        new_nums = [nums[0]]
        for i in nums[1:]:
            runnning_sum = new_nums[-1]+i
            new_nums.append(runnning_sum)
        return new_nums