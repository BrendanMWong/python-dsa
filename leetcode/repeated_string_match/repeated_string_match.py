import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rotation = math.ceil(len(b) / len(a))
        if b in (a * rotation):
            return rotation
        if b in (a * (rotation + 1)):
            return rotation + 1
        return -1