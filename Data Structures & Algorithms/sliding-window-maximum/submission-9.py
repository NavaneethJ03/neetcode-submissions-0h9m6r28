class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0 
        q = deque()

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r) # we append the indexes 
            # that is we are checking whether the first element is within the window or not
            if l > q[0]: 
                q.popleft()
            # we are checking whether we have reached the window limit or not and updating the result in the output 
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1 

            r += 1 

        return output
             

