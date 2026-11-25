class Solution {
public:


    bool valid_char(char c)
    {        
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }

    bool isPalindrome(string s) {
        // cout << valid_char(' ');
        int start = 0;
        int end = s.size() - 1;

        while (start < end)
        {
            //move start all the way to the right until it hits a valid position 
            while (valid_char(s[start]) == false && start < s.size() - 1) start++;

            //move end all the way to the left until it hits a valid position 
            while (valid_char(s[end]) == false && end >= 0) end--;

            if (start >= end)
            {
                return true;
            }


            //compare values at start idx and end idx and if they don't match, return false

            if (tolower(s[start]) != tolower(s[end]))
            {
                // cout << s[start];
                // cout << s[end];
                return false;
            }

            start++;
            end--;

        }

        return true;
    }
};
