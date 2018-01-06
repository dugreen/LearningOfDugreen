# 3sum(python解决方案)

> Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

	class Solution():
		def threeSum(nums):
			if len(nums) < 3:
				return []
			elif len(nums) == 3:
				if sum(nums) == 0:
					return [sorted(nums)]
				else:
					return []
	
			ans = []
				
			for i in len(nums) - 2:
				j = i + 1
				k = len(nums) -1
				
				while j < k:
					sum_temp = nums[i] + nums[j] + nums[k]
					if sum_temp == 0:
						ans.append((nums[i],ans[j],ans[k]))
					elif sum_temp > 0:
						k-=1
					else:
						j+=1
			return list(set(tuple(ans)))


