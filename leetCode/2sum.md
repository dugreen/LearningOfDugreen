# 2 sum问题详解(python版)

> 2 sum的求和问题一般是这样子描述的：给你一组N个数字(数字可重复), 然后给你一个常数(比如 target = 5) ，我们的goal是在这一堆数里面找到2个数字，使得这2个数字的和等于target。

***首先说明一下，本文所有的返回结果是存储在列表中的***

**具体细节可以分为以下情况**

1. 只返回一组匹配成功的组合
2. 返回多组成功的组合（实现去重）比如数组arr = [0,1,1,2,3],target=3,有result = [[]0,3],[1,2],[1,2]],因为数组中有重复的元素，故结果集中包含重复的列表元素，我们需要去除重复的元素。
3. 返回多组成功的**组合的秩**，也就是没有去重的操作。

### 情况一（只返回一组匹配成功的组合）

**解决方案一**

	class Solution:
	    def twoSum(self, nums, target):
	        """
	        :type nums: List[int]
	        :type target: int
	        :rtype: List[int]
	        """
	        if len(nums) <= 1:
	            return False
	        buff_dict = {}
	        for i in range(len(nums)):
	            if nums[i] in buff_dict:
	                return [buff_dict[nums[i]], i]
	            else:
	                buff_dict[target - nums[i]] = i

**解决方案二**
	
	class Solution:
	    def twoSum(self, nums, target):
	        """
	        :type nums: List[int]
	        :type target: int
	        :rtype: List[int]
	        """
	        if len(nums) <= 1:
	            return False

	        i = 0
	        j = len(nums) - 1
	
	        while i < j :
		        sum = li[i] + li[j]
		        if sum == target:
		            # 遇到匹配的立刻返回
		            return [li[i],li[j]]
		        elif sum < target:
		             i+=1
		        else:
		             j-=1


-----------


### 情况二（返回多组成功的组合（实现去重））

	class Solution:
		    def twoSum(self, nums, target):
		        """
		        :type nums: List[int]
		        :type target: int
		        :rtype: List[int]
		        """
		        result = []

		        if len(nums) <= 1:
		            return False

		        i = 0
		        j = len(nums) - 1
		        
		        while i < j :
			        sum = li[i] + li[j]
			        if sum == target:
			            if [li[i],li[j]] not in re:
			                result.append([li[i],li[j]])
			            i+=1
			            j-=1
			        elif sum < target:
			            i+=1
			        else:
			            j-=1
			    return result

---------------	             

### 情况三（返回多组成功的**组合的秩**）

	class Solution:
		    def twoSum(self, nums, target):
		        """
		        :type nums: List[int]
		        :type target: int
		        :rtype: List[int]
		        """
		        result = []
		        if len(nums) <= 1:
		            return False
		        
		        for i in range(len(nums)-1):
		        	for j in range(len(nums)-i-1):
		        	sum = li[i] + li[j]
			        	if sum == target:
			                result.append([i,j])

			    return result

--------------
