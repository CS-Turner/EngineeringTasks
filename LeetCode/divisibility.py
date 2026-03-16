# Q1. Ugly Number
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        for ugly in (2, 3, 5):
            while n % ugly == 0:
                n //= ugly
        if n == 1: return True
        else: return False

# Q2.

# max_value = 10 ** k - 1
# n = 1
# while n <= max_value:
#     if n % k == 0:
#         return len(str(n))
#     else:
#         n = n * 10 + 1
# return -1
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """

        def isrepunit(n):
            if n <= 0: return False
            while n > 0:
                if n % 10 != 1: return False
                n //= 10
            return True

        if isrepunit(k) True: return len(str(k)

