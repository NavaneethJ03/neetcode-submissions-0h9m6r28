class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2

        if len(A) > len(B):
            A , B = B , A

        total = len(A) + len(B)
        half = total // 2 
        l , r = 0 , len(A) - 1 

        while True:
            Amid = (l + r) // 2 
            Bmid = half - Amid - 2 

            Aleft = A[Amid] if Amid >= 0 else float('-inf')
            Aright = A[Amid + 1] if Amid + 1 < len(A) else float('inf')
            Bleft = B[Bmid] if Bmid >= 0 else float('-inf')
            Bright = B[Bmid + 1] if Bmid + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft , Bleft) + min(Aright , Bright)) / 2 
                else:
                    return min(Aright , Bright)

            elif Aleft > Bright:
                r = Amid - 1 
            else:
                l = Amid + 1 