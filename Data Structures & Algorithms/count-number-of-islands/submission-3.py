class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islandCount = 0
        row = len(grid)
        col = len(grid[0])


        def bfs(r, c):
            myq = collections.deque()
            myq.append((r,c))
            visited.add((r,c))

            while (myq):
                currR, currC = myq.pop()
                locationToCheck = [[0,1], [0,-1], [1,0], [-1,0]]
                for direction in locationToCheck:
                    newR = currR + direction[0]
                    newC = currC + direction[1]
                    if (newR in range(row) and 
                        newC in range (col) and 
                        grid[newR][newC] == "1" and 
                        (newR,newC) not in visited):
                        visited.add((newR,newC))
                        myq.append((newR,newC))
            



        for r in range(row):
            for c in range(col):
                if (grid[r][c] == "1"):
                    if (r,c) not in visited:
                        bfs(r, c)
                        islandCount += 1

        return islandCount
