class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        return 1 + self.numberOfSteps(num-1 if num % 2 != 0 else num / 2)


if __name__ == '__main__':
    r = Solution()
    num = 123
    x = r.numberOfSteps(num)
    print(x)
