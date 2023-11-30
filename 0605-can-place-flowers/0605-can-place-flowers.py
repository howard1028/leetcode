class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 檢查長度1
        if len(flowerbed) == 1:

            if flowerbed[0] == 0: 
                if n <= 1:
                    return True
                else:
                    return False
            elif flowerbed[0] == 1:
                if n <= 0:
                    return True
                else:
                    return False
            
        # 檢查頭尾
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] == 1
            n -= 1
         
        # 檢查中間  
        for i in range(1,len(flowerbed)-2,1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                print(i)
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        else:
            return False