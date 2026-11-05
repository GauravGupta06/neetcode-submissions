class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for x in range (len(nums)+1)]
        mydict = {}

        for n in nums:
            mydict[n] = 1 + mydict.get(n, 0)
        for n, c in mydict.items():
            counts[c].append(n)

        res = []
        for i in range (len(counts) - 1, 0, -1):
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res


                
















