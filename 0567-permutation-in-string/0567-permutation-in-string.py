from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)  # s1中每個字母的計數器
        temp_count_s1 = count_s1.copy()  # 複製計數器用於檢查

        left = 0
        for right in range(len(s2)):
            # 若 s2[right] 在 s1 的計數器中，減少該字母的計數
            if s2[right] in count_s1:
                temp_count_s1[s2[right]] -= 1
                if temp_count_s1[s2[right]] == 0:
                    del temp_count_s1[s2[right]]

            # 窗口大小與 s1 長度相同，檢查是否完全匹配
            if right -left + 1 == len(s1):
                # 若計數器為空，表示匹配成功
                if len(temp_count_s1) == 0: 
                    return True
                # 還沒找到完全匹配的，則移動窗口，將 left 所指向的字母還原計數
                if s2[left] in count_s1:
                    temp_count_s1[s2[left]] += 1
                    if temp_count_s1[s2[left]] == 0:
                        del temp_count_s1[s2[left]]
                left += 1
        return False
