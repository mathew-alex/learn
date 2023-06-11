class Solution:
    def two_sum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            pair_index = hashmap.get(target - num, False)
            if pair_index is not False:
                return [pair_index, index]
            hashmap[num] = index
        return []
