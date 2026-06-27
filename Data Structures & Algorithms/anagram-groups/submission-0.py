class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in d1:
                 d1[sorted_str] = [s]

            else:
                d1[sorted_str].append(s)

        l = []

        for values in d1.values():
            l.append(values)

        return l

            
        