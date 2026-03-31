class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dois ponteiros pq nesse cenario realmente a gente tem uma array desordenada
        # mas no cenario de ser ordenado algumas coisas podem ser percebidas
        # por exemplo, no caso de 6
        # [1,2,3,4]
        # 1 + 2 = 3
        # 1 + 3 = 4
        # 1 + 4 = 5
        # 2 + 1 = 3
        # 2 + 3 = 5
        # 2 + 4 = 6 --> resultado encontrado

        p1 = 0
        p2 = 1

        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if i != j and numbers[i] + numbers[j] == target:
                    return [min(i+1,j+1), max(i+1,j+1)]

        return []