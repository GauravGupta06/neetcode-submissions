class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        HDist = len(matrix[0])
        VDist = len(matrix) - 1
        output = []
        row, col = 0, -1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        currDir = 0
        while (HDist > 0 and (currDir % 2 == 0)) or (VDist > 0 and (currDir % 2 == 1)):
            stepR = directions[currDir][0]
            stepC = directions[currDir][1]
            
            # if going H
            if (currDir == 0 or currDir == 2):
                for x in range(HDist):
                    row += stepR
                    col += stepC
                    output.append(matrix[row][col])
                HDist -= 1
            
            elif (currDir == 1 or currDir == 3):
                for x in range(VDist):
                    row += stepR
                    col += stepC
                    output.append(matrix[row][col])
                VDist -= 1

            currDir = (currDir + 1) % 4

        return output