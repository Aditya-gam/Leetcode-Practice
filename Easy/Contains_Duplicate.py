class Solution:
   def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False
        
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        

if __name__ == "__main__":
    # Input the integer array
    nums = list(map(int, input().split()))
    sol = Solution()
    print(sol.containsDuplicate(nums))