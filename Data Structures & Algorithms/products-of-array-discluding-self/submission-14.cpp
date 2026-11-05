class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        //calculate the sum of all the numbers, skip if 0. 
        //keep track of number of 0s 

        //create vector of size nums
        //for each value, if more than 0 nums, set to 0
        //else if that value is 0, set to product
        //else set to product / value 

        //return vector

        int product = 1;
        int zero_count = 0;
        for (int num : nums)
        {
            if (num != 0) product *= num;
            else zero_count++;
        }

        std::vector<int> output(nums.size());

        for (int i = 0; i < nums.size(); i++)
        {
            if (zero_count > 1) output[i] = 0;
            else if (zero_count == 1)
            {
                if (nums[i] == 0) output[i] = product;
                else output[i] = 0;
            }
            else output[i] = product/nums[i];
        }

        return output;

    }
};
