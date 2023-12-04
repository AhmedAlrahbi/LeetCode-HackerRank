#for https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, nums, val):
        j = 0  
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]  
                j += 1 
                
        return j
def main():
    solution = Solution()
    nums = [3, 2, 2, 3] 
    val = 3  
    expected_nums = [2, 2] 

    j = solution.removeElement(nums, val) 
    assert j == len(expected_nums)
    nums[:j] = sorted(nums[:j])
    for i in range(j):
        assert nums[i] == expected_nums[i]

main()