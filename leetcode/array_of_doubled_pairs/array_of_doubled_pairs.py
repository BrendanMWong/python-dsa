class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key = abs)
        freq = {} #number: frequency
        for element in arr:
            freq[element] = freq.get(element, 0) + 1
        for element in arr:
            if freq[element] == 0:
                continue
            double = 2 * element
            if freq.get(double, 0) == 0:
                return False
            freq[element] -= 1
            freq[double] -= 1
        return True