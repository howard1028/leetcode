class Solution:
    def maxLength(self, arr: List[str]) -> int:

        arr_bin = []
        m = 0

        for s in arr:
            a = 0 # 目前char
            dup = 0 # 目前string內重複的

            for char in s:
                dup |= a & (1 << (ord(char) - ord('a')))
                a |= 1 << (ord(char) - ord('a'))
                # print(char , bin(a) , bin(dup))

            if dup == 0:
                arr_bin.append(a)
                m = max(m , bin(a).count("1"))
        # print(arr_bin)
                
        if len(arr_bin) == 1:
            return bin(arr_bin[0]).count("1")
        else:
            for i in range(len(arr_bin)):
                for j in range(i , len(arr_bin) , 1):
                    # 兩個比，沒有重複
                    if arr_bin[i] & arr_bin[j] == 0:
                        arr_bin.append(arr_bin[i]|arr_bin[j])
                        m = max(m , bin(arr_bin[i]|arr_bin[j]).count("1"))
            return m
