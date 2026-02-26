class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # store tuples of (row index, col index) of 1's in img1
        img1_coords = []
        # store tuples of (row index, col index) of 1's in img2
        img2_coords = []

        # length of row = len(img)
        # length of col = len(img[0])

        # img1 tuple storing
        for row in range(len(img1)):
            for col in range(len(img1[0])):
                if img1[row][col] == 1:
                    img1_coords.append((row, col))
        # img2 tuple storing
        for row in range(len(img2)):
            for col in range(len(img2[0])):
                if img2[row][col] == 1:
                    img2_coords.append((row, col))
        
        # create dict to hold (the shift done): number of times that shift aligned 1s
        shifts = {}

        # for each img1 tuple - image2 tuple, store it in dict as the tuple (x transform, y transform)
        for (x1, y1) in img1_coords:
            for (x2, y2) in img2_coords:
                transform = (x2 - x1, y2 - y1)
                # brand new tuples get the value 0 + 1 = 1, which is correct
                shifts[transform] = shifts.get(transform, 0) + 1
        
        # count how many times each translation shift aligns 1s from both images
        # the largest value in dict = the most amount of times a particular shift aligned 1s
        # example: if shift 1 to the right and 2 1's match because 2 squares matched, then value is 2
        max_overlap = 0
        for value in shifts.values():
            if value > max_overlap:
                max_overlap = value

        return max_overlap