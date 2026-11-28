class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n , 0) +1
        
        for value in hashmap.values():
            if value >1:
                return True
        return False