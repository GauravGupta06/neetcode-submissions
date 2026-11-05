class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;               // number -> count
        for (int n : nums) freq[n]++;               // missing keys start at 0

        // bucket[i] holds the numbers that appear exactly i times
        vector<vector<int>> bucket(nums.size() + 1);
        for (auto& [num, count] : freq) bucket[count].push_back(num);

        vector<int> result;
        for (int i = bucket.size() - 1; i >= 0 && (int)result.size() < k; i--) {
            for (int num : bucket[i]) {
                result.push_back(num);
                if ((int)result.size() == k) break;
            }
        }
        return result;
    }
};