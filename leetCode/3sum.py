import random

class Solution():
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self,nums):
        if  len(nums) < 3:
                return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        nums = sorted(nums)
        ans = []

        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1

            while j<k:
                temp_sum = nums[i]+nums[j]+nums[k]
                if temp_sum == 0:
                    ans.append((nums[i],nums[j],nums[k]))

                if temp_sum > 0:
                    k -= 1
                else:
                    j += 1

        return list(set(tuple(ans)))

s = Solution()
nums = [int(random.random()*10) for i in range(20)]
print(nums)
result = s.threeSum(nums)
print(result)
