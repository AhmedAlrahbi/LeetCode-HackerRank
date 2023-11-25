#for https://leetcode.com/problems/sum-of-digits-in-base-k/description/
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0 
        while n > 0:
            rem = n % k
            res += rem #suming loop outputs
            n //= k #to stop loop when n reach 0

        return res


solution = Solution()
print(solution.sumBase(34, 6)) 
print(solution.sumBase(10, 10))  