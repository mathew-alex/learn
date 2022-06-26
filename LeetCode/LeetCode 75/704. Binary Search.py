'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''
class Solution:
    def search(self, nums, target: int) -> int:
        l_index = 0
        r_index = len(nums)-1
        a = r_index // 2
        while l_index <= r_index:
            mid_index = min(l_index + a, r_index)
            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] < target:
                l_index = mid_index + 1
            else:
                r_index = mid_index - 1
            a //= 2
        return -1
