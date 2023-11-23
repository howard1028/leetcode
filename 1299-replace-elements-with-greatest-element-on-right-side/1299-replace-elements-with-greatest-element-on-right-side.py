class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        temp_max = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = temp_max
            if arr[i] > temp_max:
                temp_max = arr[i]
        return res