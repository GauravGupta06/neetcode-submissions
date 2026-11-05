class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::map<char, int>, vector<string>> wordsHash;

        for (string curr : strs)
        {
            std::map<char, int> wordHash;
            for (char letter : curr)
            {
                wordHash[letter]++;
            }
            wordsHash[wordHash].push_back(curr);
        }

        std::vector<std::vector<string>> output;
        for (const auto& [key, value] : wordsHash)
        {
            output.push_back(value);
        }
        return output;
    }
};
