class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if target > jug1+jug2:
            return False
        return target % gcd(jug1, jug2) == 0
        