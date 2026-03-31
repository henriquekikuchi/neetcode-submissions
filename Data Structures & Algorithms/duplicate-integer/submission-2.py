class Solution:
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
         i = 0
         j = i + 1
         nums = sorted(nums)

         while j < len(nums):
            if (nums[i] == nums[j]):
                return True

            i += 1
            j += 1

         return False
    """

    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))