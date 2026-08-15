class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0

        for num in nums:
            total_xor ^= num

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1 if any(nums) else 0