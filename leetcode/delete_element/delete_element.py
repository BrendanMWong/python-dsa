class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize output count
        k = 0

        # Initialize read pointer and write pointer
        read_pointer_index = 0
        write_pointer_index = 0

        # Loop while read pointer isn't out of bounds
        while read_pointer_index < len(nums):

            # Check if read pointer value = val
            if nums[read_pointer_index] != val:
                # Write read pointer value to write pointer value, mutate list
                nums[write_pointer_index] = nums[read_pointer_index]
                
                k += 1
                write_pointer_index += 1
            read_pointer_index += 1
        return k