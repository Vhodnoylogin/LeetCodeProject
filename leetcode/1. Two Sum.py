from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            if x in dict:
                dict[x] += [i]
            else:
                dict[x] = [i]
        # dict = {x: i for i, x in enumerate(nums)}
        for i in dict.keys():
            i1 = (target - i)
            v1 = dict[i].pop(0)
            if i1 in dict and len(dict[i1]) > 0:
                return [v1, dict[i1].pop(0)]
            dict[i].append(v1)
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    exp = [0, 1]
    res = Solution().twoSum(nums, target)
    print(res)
    assert Solution().twoSum(nums, target) == exp

    nums = [3, 2, 4]
    target = 6
    exp = [1, 2]
    res = Solution().twoSum(nums, target)
    print(res)
    assert Solution().twoSum(nums, target) == exp

    nums = [3, 3]
    target = 6
    exp = [0, 1]
    res = Solution().twoSum(nums, target)
    print(res)
    assert Solution().twoSum(nums, target) == exp
