class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        c = defaultdict(lambda: -1)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if k == j or i == k:
                        continue
                    key = tuple(sorted([i,j,k]))

                    if key in c.keys():
                        continue

                    c[key] = nums[i] + nums[j] + nums[k]
                    if c[key] == 0:
                        arr.append([nums[i], nums[j], nums[k]])
        
        if len(arr) == 0:
            return []

        c = set()
        for i in range(len(arr)):
           v = tuple(sorted(arr[i]))
           c.add(v)

        return list(map(lambda x: list(x), c))