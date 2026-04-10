class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        1...N rotated

        entender quais são os indices que se encaixam em ascending order
        real start index que seria a rolagem
        """
        stack = [0]

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            stack.append(i)

        ini_index = stack[0]

        return nums[ini_index]

