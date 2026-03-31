class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums = sorted(nums)

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1

        return longest
            




        
