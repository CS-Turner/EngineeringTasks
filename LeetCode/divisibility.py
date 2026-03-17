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

# Q2. repunit problem: given k, find the smallest repunit number divisible by k

class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return -1

        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k  # all the repunits up to length k, mod k
            if remainder == 0:
                return length

        return -1
