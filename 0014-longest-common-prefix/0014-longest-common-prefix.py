class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # 和第一項做比較
        prefix = strs[0]
        
        for i in range(len(prefix)):
            for string in strs[1:]:
                # check是否遍歷完或不符合
                if i == len(string) or string[i] != prefix[i]:
                    return prefix[:i]
        # 有完全符合
        return prefix