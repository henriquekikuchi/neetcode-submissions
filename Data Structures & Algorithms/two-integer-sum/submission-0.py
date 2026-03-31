class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            j=0
            while j < len(nums):
                if j == i:
                    j += 1
                    continue
                
                if nums[i] + nums[j] == target:
                    return [i, j]

                j += 1                
        