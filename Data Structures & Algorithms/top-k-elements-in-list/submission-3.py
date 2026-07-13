class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        l = []
        d1 = {}

        for i in range(len(nums)+1):
            l.append([])

        for i in nums:
            if i not in d1:
                d1[i] = 1

            else:
                d1[i] += 1

        print(d1)
        for keys,value in d1.items():
            l[value].append(keys)

        l1 = []

        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                l1.append(n)
                if len(l1) == k:
                    return l1



        
            

        