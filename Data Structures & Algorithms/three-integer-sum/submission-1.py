class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() # Sort the array 
        for i , a in enumerate(nums): # Loop to find the first variable to add 
            if a > 0 :
                break # if the first var is itself greater than zero then the sum pair cannot be formed 

            if i > 0 and a == nums[i-1]:
                continue # this is so that the duplicate values can be avoided in the ans list so we simply iterate over the duplicate items in the sorted array 

            l , r  = i + 1 , len(nums) - 1 
            # here we apply the binary search for the rest two vars for the suitable three sum pair 
            while l < r :
                summ = a + nums[l] + nums[r]
                if summ > 0:
                    r -= 1 
                elif summ < 0:
                    l += 1 
                else:
                    ans.append([a , nums[l] , nums[r]])

                    l += 1 
                    r -= 1 
                    
                    while nums[l] == nums[l-1] and l < r:
                        # this is so that , we can avoid the duplicates values in the sorted array 
                        l += 1

        return ans 