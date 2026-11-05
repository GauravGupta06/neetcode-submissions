class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> pastSums;

        for (int i = 0; i < nums.size(); i++)
        {
            int sum = target - nums[i];
            if (pastSums.contains(sum)) return {pastSums[sum], i};
            pastSums[nums[i]] = i;
        }
    }
};
