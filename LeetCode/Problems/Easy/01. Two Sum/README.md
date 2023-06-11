## `1. Two Sum` (Difficulty: Easy)


Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to 
`target`_.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

<br />

#### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

#### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

<br />

#### Constraints:

* `2 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* **Only one valid answer exists.**
 
<br />

**Follow-up:** Can you come up with an algorithm that is less than `O(n^2)` time complexity?
<hr />
<br />


> ## Solution (Python3)
> ### Approach: Use a HashMap
> #### Steps:
> 1. Create a HashMap to store the value and index of each element in the array.
> 2. Iterate through the array and check if the complement of the current element exists in the HashMap.
> 3. If the complement exists, return the indices of the current element and the complement.
> 4. If the complement does not exist, add the current element and its index to the HashMap.
> 5. If no solution exists, return an empty array.
> #### Analysis:
> * Time complexity: `O(n)`
> * Space complexity: `O(n)`
> #### Code:
> ```python
> class Solution:
>    def twoSum(self, nums: List[int], target: int) -> List[int]:
>        hashmap = {}
>        for index, num in enumerate(nums):
>            pair_index = hashmap.get(target-num, False)
>            if pair_index is not False:
>                return [pair_index, index]
>            hashmap[num] = index
>        return []

