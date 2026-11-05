class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //create map of maps that holds vector of strings  
        //for each word, crete map of letters 
        //if the map exists in the map of maps, append word 
        //take final map of maps, and append each value to output vector

        std::map<std::map<char, int>, std::vector<string>> allWords;

        for (string word:strs)
        {
            std::map<char, int> wordHash;
            for (char letter: word)
            {
                wordHash[letter]++;
            }
            allWords[wordHash].push_back(word);
        }
        vector<vector<string>> output;
        for (const auto& [key, value] : allWords)
        {
            output.push_back(value);
        }
        return output;
    }
};