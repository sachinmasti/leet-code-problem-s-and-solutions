class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        if not nums:
            return []
        
        new_nums = [nums[0]]
        for i in range(1,len(nums)):
            new_nums.append(new_nums[i-1]+nums[i])
        return new_nums