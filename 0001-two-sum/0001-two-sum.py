class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums and target ==0:
            return None

        temp_dict ={}

        for i,x in enumerate(nums):
            num = target - x

            if num in temp_dict:
                return [temp_dict[num],i]
            else:
                temp_dict[x] = i
        return None
