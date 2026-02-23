# Matrix coordinate approach

import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        # Min-heap that stores:
        # (sum of pair, index in nums1, index in nums2)
        heap = []

        # We start with the smallest possible pair (0,0)
        initial_sum = nums1[0] + nums2[0]
        heapq.heappush(heap, (initial_sum, 0, 0))

        # Track which (i, j) pairs we already added to the heap
        visited = set()
        visited.add((0, 0))

        result = []

        # Keep extracting smallest pairs until we collect k of them
        while heap and len(result) < k:

            # Get the currently smallest pair
            current_sum, index_nums1, index_nums2 = heapq.heappop(heap)

            # Add the actual numbers (not the sum) to the answer
            result.append([
                nums1[index_nums1],
                nums2[index_nums2]
            ])

            # Explore the "neighbor" below in nums1 (move down)
            next_i = index_nums1 + 1
            next_j = index_nums2

            if next_i < len(nums1) and (next_i, next_j) not in visited:
                # Compute the sum for this new pair
                new_sum = nums1[next_i] + nums2[next_j]

                # Push it into the heap so it becomes a future candidate
                heapq.heappush(heap, (new_sum, next_i, next_j))

                # Mark this coordinate as visited so we don't push it again later
                visited.add((next_i, next_j))

            # Explore the "neighbor" to the right in nums2 (move right)
            next_i = index_nums1
            next_j = index_nums2 + 1

            if next_j < len(nums2) and (next_i, next_j) not in visited:
                # Compute the sum for this new pair
                new_sum = nums1[next_i] + nums2[next_j]

                # Push it into the heap as another candidate
                heapq.heappush(heap, (new_sum, next_i, next_j))

                # Mark it visited to prevent duplicate work
                visited.add((next_i, next_j))

        return result