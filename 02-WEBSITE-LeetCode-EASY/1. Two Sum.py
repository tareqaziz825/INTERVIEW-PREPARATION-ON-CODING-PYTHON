# https://leetcode.com/problems/two-sum/description/

#  Time Complexity: O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i in range (len(nums)):
#         for j in range (i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return[i, j]


#  Time Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNum = {}
        for i in range (len(nums)):
            needNum = target - nums[i]

            if needNum in seenNum:
                return [seenNum[needNum], i]

            # dictionary_name[key] = value
            seenNum[nums[i]] = i

