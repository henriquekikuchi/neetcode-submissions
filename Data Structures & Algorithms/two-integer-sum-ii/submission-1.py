class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p2 > p1:
            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            else:
                p1 += 1

        # for i in range(0, len(numbers)):
        #     for j in range(0, len(numbers)):
        #         if i != j and numbers[i] + numbers[j] == target:
        #             return [min(i+1,j+1), max(i+1,j+1)]

        # return []