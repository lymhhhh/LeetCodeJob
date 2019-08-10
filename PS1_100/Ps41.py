'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''


class Solution:
    def firstMissingPositive(self, nums) -> int:
        if len(nums) < 1:
            return 1
        smallest = len(nums)
        largest = 0
        neg = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                neg += 1
                continue
            if smallest > nums[i]:
                smallest = nums[i]
            if largest < nums[i]:
                largest = nums[i]
        if smallest != 1:
            return 1
        size = min((len(nums) - neg), largest)
        states = [False] * size
        for i in range(len(nums)):
            if (nums[i] > 0) and (nums[i] <= size):
                states[nums[i] - 1] = True
        for i in range(len(states)):
            if not states[i]:
                return i + 1
        return size+1


sol = Solution()
print(sol.firstMissingPositive([4,3,4,1,1,4,1,4]))

'''
标题：

网址：

内容：

最初思路：使用最小最大之间设置空间查看状态

存在问题：使用了额外空间

参考思路：交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组，复杂度为O(n)。

最终思路：

改进方向：

代码：

反思与总结：
'''
