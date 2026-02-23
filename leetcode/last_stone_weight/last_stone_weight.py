import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-element for element in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            heaviest_weight = heapq.heappop(heap)
            second_heaviest_weight = heapq.heappop(heap)
            if heaviest_weight != second_heaviest_weight:
                new_weight = second_heaviest_weight - heaviest_weight
                heapq.heappush(heap, -1 * new_weight)
        if len(heap) == 1:
            return abs(heap[0])
        return 0