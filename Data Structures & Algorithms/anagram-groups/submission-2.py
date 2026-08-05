class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if not d1:
                d1[sorted_text] = [i]

            elif sorted_text not in d1:
                d1[sorted_text] = [i]

            else:
                d1[sorted_text].append(i)

        l1 = []

        for i in d1.values():
            l2 = []
            for j in range(len(i)):
                l2.append(strs[i[j]])

            l1.append(l2)

        return l1
                



        

        