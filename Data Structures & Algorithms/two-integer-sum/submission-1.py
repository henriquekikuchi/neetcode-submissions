class Solution:
    """
    first solution:
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
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference in items.keys():
                return [min(i, items[difference]), max(i, items[difference])]
            
            items[nums[i]] = i
            
