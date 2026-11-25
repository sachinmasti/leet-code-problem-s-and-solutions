class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        sort_nums = sorted(nums)

        left,right = 0,len(sort_nums) - 1
        total_count = 0

        while left < right:
            total = sort_nums[left] + sort_nums[right]

            if total < target:
                total_count += right - left
                left +=1
            else:
                right -=1
        return total_count