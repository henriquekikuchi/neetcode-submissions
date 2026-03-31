# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        state_history = []
        
        for i in range(0,len(pairs)):
            for j in range(i,-1,-1):
                if pairs[i].key < pairs[j].key:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i = j
            state_history.append(pairs[:])

        return state_history 


        