class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for nb in nums_set:
            if nb - 1 in nums_set:
                continue

            length = 1

            while nb + length in nums_set:
                length += 1

            max_len = max(max_len, length)

        return max_len