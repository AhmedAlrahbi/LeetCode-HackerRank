#for https://leetcode.com/problems/sqrtx/
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
solution = Solution()
x1 = 4
print(solution.mySqrt(x1))  
x2 = 8
print(solution.mySqrt(x2))  