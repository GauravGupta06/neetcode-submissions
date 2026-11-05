class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_hash;
        std::unordered_map<char, int> t_hash;

        for (char letter:s) s_hash[letter]++;
        for (char letter:t) t_hash[letter]++;

        return s_hash == t_hash;
    }
};
