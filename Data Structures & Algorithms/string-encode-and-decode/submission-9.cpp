class Solution {
public:

    string encode(vector<string>& strs) {
        std::string output;
        for (string str:strs)
        {
            output += to_string(str.size()) + '#' + str;
        }
        
        // cout << output;
        return output;
    }

    vector<string> decode(string s) {
        int i = 0;
        int j = 0;
        std::vector<string> output;
        
        while (j < s.size())
        {
            while (s[j] != '#') j++;
            int size = stoi(s.substr(i, j));
            output.push_back(s.substr(j + 1, size));
            j = j + 1 + size;
            i = j;
        }
        return output;

    }
};
