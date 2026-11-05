class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> num_set;

        for (int num:nums)
        {
            if (num_set.contains(num)) return true;
            num_set.insert(num);
        }
        return false;

    }
};