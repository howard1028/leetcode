class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_set = set(nums)
        res = []

        print(nums_set)

        for i in range(1 , len(nums)+1 , 1):
            if i not in nums_set:
                res.append(i)

        return res

        # res = []
        # for num in nums:
        #     index = abs(num) - 1
        #     nums[index] = -abs(nums[index])

        # print(nums)
