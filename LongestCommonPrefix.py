class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        if len(strs) == 1:
            return strs[0]
        for i in range(len(min(strs))):
            temp = strs[0][i]
            counter = 0
            for j in range(len(strs)):
                if temp == strs[j][i]:
                    counter += 1
                    if counter == len(strs):
                        result += temp
                else:
                    return result
        return result
print(111)