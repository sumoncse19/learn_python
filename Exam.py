print(type(int(12.3)))
print('hello'.upper())
print(str(1)+str(1))
print(type(1/1))

from typing import List

nums = [1, 0, 1, 1]
k = 1

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            print(num, i)
            if(num in index_map and i - index_map[num] <= k):
                print('inner if', index_map, i, index_map[num])
                return True
            index_map[num] = i
            print(index_map)
        return False

# Create an instance of the Solution class
solution = Solution()
# Call the method and print the result
print(solution.containsNearbyDuplicate(nums, k))