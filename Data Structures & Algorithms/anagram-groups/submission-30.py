class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashOfWords = {}
        for word in strs:
            wordHash = {}
            for letter in word:
                if letter in wordHash:
                    wordHash[letter] += 1
                else:
                    wordHash[letter] = 1
            key = tuple(sorted(wordHash.items()))

            if key in hashOfWords:
                hashOfWords[key].append(word)
            else:
                hashOfWords[key] = [word]
        return list(hashOfWords.values())
                
                