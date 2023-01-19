# Definition for singly-linked list.
import math

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.__this = self

    def __iter__(self):
        self.__this = self
        return self

    def __next__(self):
        if self.__this is None:
            raise StopIteration
        res = self.__this.val
        self.__this = self.__this.next
        return res

    def __str__(self):
        return str([x for x in self])


def initListNodes(list: List) -> Optional[ListNode]:
    prev = None
    for x in reversed(list):
        prev = ListNode(x, prev)
    return prev


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        x = [head]
        head = head.next
        while head:
            x.append(head)
            head = head.next
        i = len(x)
        if i == 1:
            return x[0]
        i = int(math.ceil((i+1) / 2))-1
        return x[i]


if __name__ == '__main__':
    list = [1,2,3,4,5,6]
    # print(list, initListNodes(list))
    x = initListNodes(list)
    print(x)
    res = Solution().middleNode(x)
    print(res)