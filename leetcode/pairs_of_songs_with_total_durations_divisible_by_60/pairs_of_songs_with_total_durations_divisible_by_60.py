# correct version
class Solution:
    def numPairsDivisibleBy60(self, time):
        # Store how many times each remainder (mod 60) has appeared
        remainder_count = {}
        output = 0

        # Loop through each song duration once
        for duration in time:

            # Get the remainder when dividing by 60
            remainder = duration % 60

            # Find what remainder would make this sum divisible by 60
            complement = (60 - remainder) % 60

            # If we've already seen the complement,
            # then those previous songs form valid pairs with this one
            if complement in remainder_count:
                output += remainder_count[complement]

            # Record this remainder for future songs
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return output

# this version doesn't work because it's too slow
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # pointers are indexes
        pointer1 = 0
        pointer2 = 0
        output = 0
        while pointer1 < len(time):
            pointer2 = pointer1 + 1
            while pointer2 < len(time):
                if (time[pointer1] + time[pointer2]) % 60 == 0:
                    output += 1
                pointer2 += 1
            pointer1 += 1
        return output