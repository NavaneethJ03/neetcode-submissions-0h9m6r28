class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        w1 = {}
        w2 = {}

        for c in s1:
            w1[c] = 1 + w1.get(c , 0)


        k = len(s1)
        l = 0 
        for i in range(k):
            c = s2[i]
            w2[c] = 1 + w2.get(c , 0)

        
        if w1 == w2:
            return True 

        for i in range(k , len(s2)):
            c = s2[i]
            w2[c] = 1 + w2.get(c , 0)
            if w2[s2[l]] == 1:
                del w2[s2[l]]
            else:
                w2[s2[l]] = -1 + w2.get(s2[l] , 0)

            l += 1 

            if w1 == w2:
                return True 

            
        return False 

                
