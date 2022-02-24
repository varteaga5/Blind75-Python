"""
Two Sum
given an array of integers, return indices of the two numbers such that they add up to a specific target.

you may assume that each input would have exactly one solution, and you may not use the same element twice

example:
given nums = [2, 3, 11, 15], target = 9,

because nums[0] + nums[1] = 2 + 7 = 9,

return [0,1]

"""

class solution:
    def two_sum(self, nums: [2, 3, 11, 15], target: 9) -> [int]:
        # hash map of each element that comes before the current element
        prevMap = {} # val : index
        # iterate over every value in the array, 
        for i, n in enumerate(nums):
            diff = target - n # find the difference
            if diff in prevMap: # check if difference is already in the hash map
                return [prevMap[diff], i]
            prevMap[n] = i # if solution is not found update hash map
        return 