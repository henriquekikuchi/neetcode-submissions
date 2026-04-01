class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [ 0 for i in range(len(temperatures))]
        for i in range(0,len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack[i] = j-i
                    break
            

        return stack
