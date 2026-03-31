class Solution:
    # constraints:
    """
    defaultdict
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = defaultdict(lambda: -1)

        for i in range(0, len(nums)):
            diff = target - nums[i]
            res = hs[diff]
            if res == -1:
                hs[nums[i]] = i
            else:
                return [i, res] if i < res else [res, i]
