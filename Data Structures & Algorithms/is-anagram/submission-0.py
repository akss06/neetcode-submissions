class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for a in s:
            if a not in d1:
                d1[a] = 1

            else:
                d1[a] += 1

        for a in t:
            if a not in d2:
                d2[a] = 1

            else:
                d2[a] += 1

        return (d1==d2)


        

        