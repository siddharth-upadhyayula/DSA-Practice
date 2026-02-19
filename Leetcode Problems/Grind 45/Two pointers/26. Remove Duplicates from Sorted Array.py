class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1

        while fast<len(nums):
            if nums[fast] == nums[slow]:
                nums.remove(nums[slow])
            else:
                fast+=1
                slow+=1
                