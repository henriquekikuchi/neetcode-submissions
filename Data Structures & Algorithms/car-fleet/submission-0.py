class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calcular tempos

        tempos = []

        for i in range(len(position)):
            tempo = (target - position[i]) / speed[i]
            tempos.append((position[i], tempo))

        if not tempos:
            return 0

        tempos = sorted(tempos, key = lambda x: x[0], reverse=True)

        fleet = tempos[0][1]
        totalFleets = 1

        for i in range(1, len(tempos)):
           if fleet < tempos[i][1]:
            totalFleets += 1
            fleet = tempos[i][1]

        return totalFleets