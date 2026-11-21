class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        if not nums:
            return []
        
        new_nums = [nums[0]]
        for i in nums[1:]:
            new_nums.append(new_nums[-1]+i)
        return new_nums