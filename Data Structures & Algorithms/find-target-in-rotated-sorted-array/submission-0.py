class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        """
        nums = [4,5,6,7,0,1,2]
        target = 5

        mid = 3, left = 0, right = 6

        7 != 5
        7 > 2
        4 < 5 < 7

        left = 0, right = 2, mid = 1

        [4,5,6]

        5 < 6

        5 
        """
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

            