class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //create set for rows
        //create set for cols 
        //create set for sub-boxes

        //loop through each row, and add to set, if dup found, return false
        //loop through each col and add to set, if dup found return false
        //loop through the three boxes using two nested for loops, adding each to set
        //if dup found return false 

        //time complexity: O(n^2)
        //space complexity O(n^2) , n being the length of one side. 

        std::vector<std::set<char>> rowSets(9);
        std::vector<std::set<char>> colSets(9);
        std::vector<std::set<char>> boxSets(9);

        for (int r = 0; r < 9; r++)
        {
            for (int pos = 0; pos < 9; pos++)
            {
                char value = board[r][pos];
                if (value != '.')
                {
                    if (rowSets[r].contains(value)) return false;
                    rowSets[r].insert(value);
                }
            }
        }

        for (int c = 0; c < 9; c++)
        {
            for (int pos = 0; pos < 9; pos++)
            {
                char value = board[pos][c];
                if (value != '.')
                {
                    if (colSets[c].contains(value)) return false;
                    colSets[c].insert(value);
                }
            }
        }

        int idx = 0;
        for (int r = 0; r < 3; r++)
        {
           for (int c = 0; c < 3; c++)
            {
                for (int x = 0; x < 3; x++)
                {
                    for (int y = 0; y < 3; y++)
                    {
                        char value = board[3*r + x][3*c + y];
                        if (value != '.')
                        {
                            if (boxSets[idx].contains(value)) return false;
                            boxSets[idx].insert(value);
                        }
                    }
                }
                idx++;
            } 
        }

        return true;



        
    }
};
