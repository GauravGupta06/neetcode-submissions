class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list) 

        for word in strs:
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            x[tuple(letters)].append(word)

        return x.values()
        
            


