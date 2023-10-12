class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        #startTime[i]:第i個人開始寫作業時間，queryTime:時間點有幾個在寫作業
        count = 0 #正在寫的人數
        for i in range(len(startTime)): #跑list的長度次
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                count += 1
            
        return count