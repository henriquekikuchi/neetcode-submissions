# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        state_history = []

        def get_pairs(format_func = None):
            if not format_func:
                return [Pair(pair.key, pair.value) for pair in pairs]
            return [format_func(pair) for pair in pairs]

        for i in range(0,len(pairs)):
            for j in range(i,-1,-1):
                if pairs[i].key < pairs[j].key:
                    tmp = Pair(pairs[i].key, pairs[i].value)
                    pairs[i] = pairs[j]
                    pairs[j] = tmp
                    i = j
            state_history.append(get_pairs())

        return state_history 


        