class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        
        for i in range(0, len(nums)):
            rp = 1
            for j in range(0, len(nums)):
                if i == j:
                    continue

                rp *= nums[j]
            results.append(rp)

        return results
