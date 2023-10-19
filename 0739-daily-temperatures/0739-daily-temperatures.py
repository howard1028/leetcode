class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures) 
        answer = [0] * n
        stack = [] # 存index

        for i in range(n):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i-j
            stack.append(i)

        return answer
