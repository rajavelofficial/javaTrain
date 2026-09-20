class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s):
            reverse_value = 26 - (ord(ch) - ord('a'))
            position = i + 1
            total += reverse_value * position

        return total