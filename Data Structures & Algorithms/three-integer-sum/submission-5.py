class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        triplets = []

        for i,a in enumerate(nums):
            target = -a
            left=i+1
            right=n-1

            if i > 0 and a == nums[i-1]:
                continue

            while left < right:
                comp = nums[left]+nums[right]
                if comp > target:
                    right-=1
                elif comp < target:
                    left+=1
                else:
                    triplets.append([a, nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1

        return triplets