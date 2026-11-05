class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash table of numbers and frequencies 
        # convert that hash table into a sorted tuple using the value as the sorting key
        # query the k top values in the sorted tuple and append values to a list 
        # return list. 

        myHash = {}
        for num in nums:
            if num in myHash:
                myHash[num] += 1
            else:
                myHash[num] = 1
        myTup = tuple(sorted(myHash.items(), key = lambda item: item[1], reverse = True))

        output = []
        for x in range (k):
            output.append(myTup[x][0])
        return output
            
        

