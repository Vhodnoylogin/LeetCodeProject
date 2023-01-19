from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    return max(sum(i) for i in accounts)


if __name__ == '__main__':
    nums = [[1, 2, 3], [3, 2, 1]]
    x = maximumWealth(nums)
    print(x)
