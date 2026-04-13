class TimeMap:

    def __init__(self):
        self.pairs = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.pairs.get(key, None)

        if values is None:
            return ""

        left = 0
        right = len(values) - 1
        
        better_choice = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                left = mid + 1
                better_choice = values[mid][0]
            else:
                right = mid - 1

        return better_choice