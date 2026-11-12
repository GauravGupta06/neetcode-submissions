class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> shash;
        std::unordered_map<char, int> thash;
        for (char c : s) shash[c]++;
        for (char c : t) thash[c]++;
        return shash == thash;
    }
};
