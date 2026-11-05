class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        returnList = []
        for word in strs:
            myTup = tuple(sorted(Counter(word).items()) )
            if myTup in hashTable:
                hashTable[myTup].append(word)
            else:
                hashTable[myTup] = [word]

        for listn in hashTable.values():
            returnList.append(listn)

        return returnList


            
        