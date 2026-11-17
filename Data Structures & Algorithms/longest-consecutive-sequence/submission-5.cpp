class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        //find all starting numbers for a sequence 
        //for each starting number, build the entire sequence 
        //store max length 

        std::set<int> numsHash(nums.begin(), nums.end());
        std::vector<int> startingNums;
        int maxConsec = 0;
        for (int num : nums)
        {
            if (!(numsHash.contains(num - 1))) startingNums.push_back(num);
        }

        for (int num : startingNums)
        {
            int currConsec = 1;
            int curr = num;
            while (numsHash.contains(curr + 1))
            {
                currConsec++;
                curr++;
            }
            if (currConsec > maxConsec) maxConsec = currConsec;
        }

        return maxConsec;
        
    }
};
