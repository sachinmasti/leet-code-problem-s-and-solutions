class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        writer = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[writer - 1]:
                nums[writer] = nums[i]
                writer += 1
        return writer