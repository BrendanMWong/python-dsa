class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Index pointers
        nums1_read = m - 1
        nums2_read = n - 1
        nums1_write = m + n - 1

        while nums2_read >= 0:
            if nums1_read >= 0 and nums1[nums1_read] > nums2[nums2_read]:
                nums1[nums1_write] = nums1[nums1_read]
                nums1_read -= 1
                nums1_write -= 1
            else:
                nums1[nums1_write] = nums2[nums2_read]
                nums2_read -= 1
                nums1_write -= 1
