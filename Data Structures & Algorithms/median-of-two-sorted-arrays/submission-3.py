class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2 
        if len(A) > len(B):
            A , B = B , A
        total = len(A) + len(B)
        half = total // 2 

        left , right = 0 , len(A) - 1 # This is because we are performing BS on the least Array 
        while True:
            A_mid = (left + right) // 2 
            B_mid = half - A_mid - 2 # -2 because there is zero indexing for both half and A_mid 

            Aleft = A[A_mid] if A_mid >= 0 else float('-inf')
            Aright = A[A_mid + 1] if A_mid + 1 < len(A) else float("inf")
            Bleft = B[B_mid] if B_mid >= 0 else float('-inf')
            Bright = B[B_mid + 1] if B_mid + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright , Bright)
                else :
                    return (max(Aleft , Bleft) + min(Aright , Bright)) / 2 

            elif Aleft > Bright:
                right = A_mid - 1 
            else:
                left = A_mid + 1 
