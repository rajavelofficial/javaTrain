class Solution:
    def longestSubsequence(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        if xor:
            return len(nums)

        return len(nums) - 1 if any(nums) else 0