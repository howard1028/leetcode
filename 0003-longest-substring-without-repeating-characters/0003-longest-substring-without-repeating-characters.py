class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        current_length = 0
        appeared_words = {} # 紀錄每個字元最後出現的索引
        start = 0


        for i,char in enumerate(s):
            # 有重複，且出現位置在start後，則重新計算長度
            if char in appeared_words and appeared_words[char] >= start:
                start = appeared_words[char] + 1
                current_length = i - start + 1 
            # 沒重複，長度+1
            else:
                current_length += 1
            # 出現的反著放進dict
            appeared_words[char] = i
            max_length = max(max_length,current_length)
        return max_length