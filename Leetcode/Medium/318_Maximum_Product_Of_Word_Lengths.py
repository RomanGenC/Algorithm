from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = len(words)
        maximum = 0
        for i in range(length):
            for j in range(i, length):
                if set(words[i]) & set(words[j]):
                    continue

                maximum = max(maximum, len(words[i]) * len(words[j]))

        return maximum
