class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        for i, Str in enumerate(strs):
            arr.append([sorted(Str), i])
        arr.sort()
        ans = []
        ls = [strs[arr[0][1]]]
        for i in range(1, len(strs)):
            if (arr[i][0] == arr[i-1][0]):
                ls.append(strs[arr[i][1]])
            else:
                ans.append(ls)
                ls = [strs[arr[i][1]]]
        ans.append(ls)
        return ans
