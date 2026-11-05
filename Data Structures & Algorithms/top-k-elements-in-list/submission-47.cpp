class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> numFreq;
        for (int num : nums) numFreq[num]++;

        std::vector<std::vector<int>> orderedNums(nums.size() + 1);
        for (const auto& [num , freq] : numFreq)
        {
            orderedNums[freq].push_back(num);
        }

        std::vector<int> output;

        for (int i = nums.size(); i > 0 ; i--)
        {
            
            for (int num : orderedNums[i])
            {
                output.push_back(num);
                if (output.size() == k) return output;
            }
                
            
        }

        
    }
};
