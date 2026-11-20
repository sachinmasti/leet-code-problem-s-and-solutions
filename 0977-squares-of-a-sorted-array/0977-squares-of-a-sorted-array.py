class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) -1
        index_pointer = len(nums) - 1
        new_list = [None] * len(nums)

        while left <= right:
            left_square = nums[left] **2
            right_sqaure = nums[right] **2

            if right_sqaure > left_square:
                new_list[index_pointer] = right_sqaure
                right -= 1
                index_pointer -=1
            elif left_square > right_sqaure:
                new_list[index_pointer] = left_square
                left +=1
                index_pointer -=1
            else:
                new_list[index_pointer] = left_square
                right -= 1
                index_pointer -=1

        return new_list