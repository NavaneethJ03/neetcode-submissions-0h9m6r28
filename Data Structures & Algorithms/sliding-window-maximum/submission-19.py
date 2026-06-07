class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = r = 0 

        while r < len(nums):
            while q and nums[r] >= nums[q[-1]]: # remove all the unnecessary idx keeping the max in front
                q.pop()
            q.append(r)

            if l > q[0]: # checking whether the left index is valid or not 
                q.popleft()

            if r + 1 >= k: # we reach the first kth segment 
                res.append(nums[q[0]])
                l += 1 

            r += 1 
        return res