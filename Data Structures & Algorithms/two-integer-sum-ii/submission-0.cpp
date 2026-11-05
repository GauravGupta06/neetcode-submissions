class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::unordered_map<int, int> alrSeen;

        for (int i = 0; i < numbers.size() ; i++)
        {
            int sub = target - numbers[i];
            if (alrSeen.contains(sub)) return {alrSeen[sub], i+1};
            alrSeen[numbers[i]] = i+1;
        }
    }
};
