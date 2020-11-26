# TLE
class Solution1:
    def waysToMakeFair(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            newArr = nums[:i] + nums[i+1:]
            print(newArr)
            
            if self.fair(newArr):
                count += 1
                
        
        return count 
    
    def fair(self, newArr):
        even = 0 
        odd  = 0
        
        for i in range(len(newArr)):
            if i % 2 == 0:
                even += newArr[i]
            else:
                odd += newArr[i]
                
        return even == odd
