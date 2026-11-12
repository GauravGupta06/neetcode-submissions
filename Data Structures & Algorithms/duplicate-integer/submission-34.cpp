class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> alrSeen;
        for (int num: nums)
        {
            if(alrSeen.contains(num)) return true;
            alrSeen.insert(num);
        }
        return false;
    }
};