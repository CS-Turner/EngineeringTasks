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

#Q3 Self dividing numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        self_dividing = []
        number = left
        while number <= right:
            remainder = number  # temp copy to compute with
            jump_value = 0  # place value of skip, initially 0
            is_valid = True
            multiplier = 1  # power of ten tracker to identify the position of a zero

            while remainder > 0:
                digit = remainder % 10  # the ones digit of the remainder
                if digit == 0:
                    is_valid = False
                    jump_value = multiplier  # place value of the zero
                elif is_valid and number % digit != 0:
                    is_valid = False

                remainder //= 10
                multiplier *= 10

            if is_valid:
                self_dividing.append(number)
                number += 1

            elif jump_value > 0:
                number = (number // (jump_value * 10)) * jump_value * 10 + (jump_value * 10 - 1) // 9

            else:
                number += 1
        return self_dividing