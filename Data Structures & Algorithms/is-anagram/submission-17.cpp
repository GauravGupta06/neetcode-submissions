class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_hash;
        std::unordered_map<char, int> t_hash;

        for (char val:s)
        {
            if (s_hash.contains(val))
            {
                s_hash[val]++;
            }
            else
            {
                s_hash.emplace(val, 1);
            }
        }

        for (char val:t)
        {
            if (t_hash.contains(val))
            {
                t_hash[val]++;
            }
            else
            {
                t_hash.emplace(val, 1);
            }
        }

        
        return t_hash == s_hash;

    }
};
