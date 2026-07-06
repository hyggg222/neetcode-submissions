class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for Str in strs:
            ls = [0] * 26
            for char in Str:
                ls[ord(char) - ord('a')] += 1
            hashVal = tuple(ls)
            if (hashVal not in ans):
                ans[hashVal] = []
            ans[hashVal].append(Str)
        return list(ans.values())