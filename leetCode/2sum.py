class Solution():
    @classmethod
    def twoSum(self,nums):
        length = len(nums)
        if length < 2:
            return []
        elif length == 2:
            if sum(nums) == 10:
                return [sorted(nums)]
            else:
                return []

        nums = sorted(nums)

        i = 0
        j = length-1

        ans = []
        while i<j:
            temp_sum = nums[i]+nums[j]
            if temp_sum == 10:
                ans.append([nums[i],nums[j]])
            elif temp_sum > 10:
                k -= 1
            else:
                i += 1
        return list(set(tuple(ans)))


numbers = [5,5]
print(numbers)
result = Solution.twoSum(numbers)
print(result)

