class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize count
        k = 1

        # Initialize read pointer and write pointer
        read_pointer_index = 1
        write_pointer_index = 1

        # Loop until read pointer is out of bounds
        while read_pointer_index < len(nums):

            # Check index before read pointer
            if nums[read_pointer_index] != nums[read_pointer_index - 1]:
                # Set write pointer value to read pointer value, mutate list
                nums[write_pointer_index] = nums[read_pointer_index]

                k += 1
                write_pointer_index += 1
            read_pointer_index += 1
        return k