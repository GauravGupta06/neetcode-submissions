class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::map<char, int>, std::vector<string>> allWords;

        for (string word:strs)
        {
            std::map<char, int> wordhash;
            for (char letter:word)
            {
                wordhash[letter]++;
            }
            allWords[wordhash].push_back(word);
        }
        std::vector<std::vector<string>> output;
        for (const auto& [key, value]:allWords)
        {
            output.push_back(value);
        }
        return output;
    }
};
