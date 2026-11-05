class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        myList = [[] for i in range (len(nums) + 1)]

        for num in nums:
            hashTable[num] = hashTable.get(num, 0) + 1
        
        for number, frequency in hashTable.items():
            myList[frequency].append(number)
        
        returnList = []
        for i in range (len(nums), 0, -1):
            for number in myList[i]:
                returnList.append(number)
                if (len(returnList) == k):
                    return returnList
        return returnList
         

        

            



        


        


        
