class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int productOfAll = 1;
        int zeroExists = 0;
        for (int num: nums) 
        {
            if (num != 0) 
            {
                productOfAll *= num;
                
            }
            else
            {
                zeroExists++;
            }
        }
        vector<int> output(nums.size());
        for (int i = 0; i < nums.size() ; i++)
        {
            if (zeroExists > 1)
            {
                output[i] = 0;
            }
            else if (nums[i] == 0) output[i] = productOfAll;
            else if (zeroExists == 1)
            {
                output[i] = 0;
            }
            else
            {
                output[i] = productOfAll/nums[i];
            }
            
        }
        return output;
    }
};
