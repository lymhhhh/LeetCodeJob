'''
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        i = 0
        while i < len(nums):
            #print(i, ":", a, b, nums)
            if nums[i] == 0:
                if a != i:
                    temp = nums[i]
                    nums[i] = nums[a]
                    nums[a] = temp
                    if nums[i]==1:
                        i-=1
                        b-=1
                a += 1
                b += 1
            elif nums[i] == 1:
                if b != i:
                    temp = nums[i]
                    nums[i] = nums[b]
                    nums[b] = temp
                b += 1
            i += 1

nums = [2, 0, 2, 1, 1, 0, 2, 2, 2, 2, 1, 2,0]
Solution().sortColors(nums)
print(nums)
