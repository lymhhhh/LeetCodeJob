'''
128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

'''
# 桶排序
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=0:
            return 0
        right = max(nums)
        left = min(nums)
        a = [0 for _ in range(right-left+1)]
        for i in range(len(nums)):
            a[nums[i]-left] += 1
        m = 0
        s = 0
        for i in range(len(a)):
            if a[i]>0:
                s+=1
            else:
                if s>m:
                    m = s
                s = 0
        if s>m:
            m = s
        return m
'''
'''
Algorithm

This optimized algorithm contains only two changes from the brute force approach: 
the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups, and we only attempt to build sequences from numbers that are not already part of a longer sequence. 
This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.

与我自己的思路大致相似，hash set可以缩减空间消耗
'''
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

print(Solution().longestConsecutive([0]))
