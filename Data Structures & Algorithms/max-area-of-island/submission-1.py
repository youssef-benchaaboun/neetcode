class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        land_list={(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y]==1}
        def dfs_count(land_list:list,curent:tuple)->int:
            x,y=curent
            stack=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            r=1
            while(stack):
                nxt=stack.pop()
                x,y=nxt
                if nxt in land_list:
                    land_list.remove(nxt)
                    r +=1
                    stack.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
            return r
        r=0
        while land_list:
            curent=land_list.pop()
            c=dfs_count(land_list,curent)
            if c >r:
                r=c
        return r