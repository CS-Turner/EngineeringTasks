from math import sqrt

## Q1. Can Make Arithmetic Progression From Sequence
    # A sequence of numbers is called an arithmetic progression if the difference between
    # any two consecutive elements is the same.
    # Given an array of numbers arr, return true if the array can be rearranged to form
    # an arithmetic progression. Otherwise, return false.

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)
        if length < 2: return True

        maximum = max(arr)
        minimum = min(arr)

        # diff = 0, true
        if minimum == maximum: return True

        # difference can't be found (integer)
        if (maximum - minimum) % (length - 1) != 0: return False

        difference = (maximum - minimum) // (length - 1)

        i = 0
        while i < length:
            if arr[i] == minimum + i * difference: # in the correct position, and arithmetic
                i += 1
            else:
                if (arr[i] - minimum) % difference != 0: # observed not arithmetic
                    return False
                position = (arr[i] - minimum) // difference # incorrect position, where should it be
                if arr[position] == arr[i]: return False # duplicate value in array
                else:
                    arr[position], arr[i] = arr[i], arr[position] # move it to the correct position
        return True




        # arr.sort()
        #
        # difference = arr[1] - arr[0]
        # for i in range(2, len(arr)):
        #     if arr[i] - arr[i - 1] != difference:
        #         return False
        # return True



## Q2. Find the Pivot Integer

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Gauss' sum from 1 to n
        sum_to_n = int(n*(n+1)/2)

        k = int(sqrt(sum_to_n))
        if k**2 == sum_to_n: return k
        else: return -1

# Q3. Determine if the given integer is a palindrome
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        digits_as_string = str(x)
        digits_reversed = digits_as_string[::-1]

        if digits_as_string == digits_reversed: return True
        else: return False