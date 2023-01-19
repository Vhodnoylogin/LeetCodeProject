from typing import List


def runningSum(nums: List[int]) -> List[int]:
    return [sum(nums[0:i + 1]) for i, x in enumerate(nums)]


if __name__ == '__main__':
    nums = [1, 5, 7, 2]
    x = runningSum(nums)
    print(x)
    # print(nums[1:2])
    # for i, x in enumerate(nums):
    #     print(i, x, nums[0:i+1], sum(nums[0:i+1]))
