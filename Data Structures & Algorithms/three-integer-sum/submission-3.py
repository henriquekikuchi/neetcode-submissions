class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos = defaultdict(set)
        res = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                diff = -(nums[i] + nums[j])
                idxs = list(filter(lambda x: x != i and x != j, pos[diff]))
                if len(idxs) > 0:
                    idx = idxs.pop()
                    res.append((nums[i],nums[j],nums[idx]))
                else:
                    pos[nums[i]].add(i)
                    pos[nums[j]].add(j)

        return list(map(list,set(map(lambda x: tuple(sorted(x)), res))))

                