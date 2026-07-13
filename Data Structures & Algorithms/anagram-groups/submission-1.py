

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d1 = {}
        
        l = []

        for word in strs:
            l.append("".join(sorted(word)))

        for i in range(len(l)):
            if l[i] not in d1:    
                d1[l[i]] = [strs[i]]

            else:
                d1[l[i]].append(strs[i])

        print(d1)

        l1 = []

        for i in d1.values():
            l1.append(i)

        return l1
        
            
            

                

        
            

        
        
        