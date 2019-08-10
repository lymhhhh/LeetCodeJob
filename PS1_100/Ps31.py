'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1: find the change number whose last numbers are largest order
        i = len(nums)-1
        while i >= 1:
            if nums[i-1]<nums[i]:
                break
            i -= 1
        if i == 0:
            nums.sort()
            return
        i -= 1
        # step 2: start at number i, find the smallest number which is bigger than the number i
        smallest = nums[i]+1
        t = i + 1
        index = i + 1
        while t < len(nums):
            if nums[t] > nums[i] and smallest > nums[i]:
                smallest = nums[t]
                index = t
            t += 1

        nums[i], nums[index] = nums[index], nums[i]
        # step 3: order the rest of the numbers(after number i) smallest(sort the numbers after i)
        a = nums[i+1:len(nums)]
        a.sort()
        nums[i+1:len(nums)] = a


sol = Solution()
a = [4, 3, 2, 1]
for i in range(10):
    sol.nextPermutation(a)
    print(a)
