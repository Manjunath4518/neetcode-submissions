class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        s = []

        for p, sp in cars:
            time = (target - p) / sp

            if not s or time > s[-1]:
                s.append(time)

        return len(s)