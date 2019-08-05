'''
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        # 老解法，从前往后，大的后移
        # 改进解法：从后往前比较，直接插入值
        i = 0
        j = 0
        while i < len(nums1) and j < n:
            #print(i, j, nums1)
            if nums1[i] > nums2[j]:
                # move the numbers of nums1 which is after [i] 1 step, and then insert the nums2[j] into nums1 at [i]
                k = len(nums1) - 1
                while k > i:
                    nums1[k] = nums1[k - 1]
                    k -= 1
                nums1[i] = nums2[j]
                i += 1
                j += 1
            else:
                #print(i,(m+j))
                if i < m+j:
                    i += 1
                else:
                    while i < len(nums1) and j < n:
                        nums1[i] = nums2[j]
                        i += 1
                        j += 1
        return
        '''
            i, j, k = m-1, n-1, m+n-1
            while i>=0 and j>=0:
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
            j += 1
            if j > 0:
                nums1[:j] = nums2[:j]
        '''



sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
print(nums1)
