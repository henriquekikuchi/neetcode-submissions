class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(lambda: -1)

        for i in range(len(nums)):
            diff = target - nums[i]
            if d[diff] != -1:
                return [min(d[diff], i), max(d[diff], i)]
            else:
                d[nums[i]] = i

        return []