from typing import List


def fizzBuzz(n: int) -> List[str]:
    def gett(n: int) -> str:
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        if n % 3 == 0:
            return "Fizz"
        if n % 5 == 0:
            return "Buzz"
        return str(n)
    return [gett(i+1) for i in range(n)]


if __name__ == '__main__':
    num = 15
    x = fizzBuzz(num)
    print(x)
