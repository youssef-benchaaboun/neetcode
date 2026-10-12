class Solution:
    def dfs_solution(self,land_list:set[tuple],grid:list[list[str]],current:tuple[int,int]):
        x,y=current
        stack_list=[(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        while(stack_list):
            nxt=stack_list.pop()
            x,y=nxt
            if nxt in land_list:
                land_list.remove(nxt)
                stack_list.extend([(x+1,y),(x-1,y),(x,y-1),(x,y+1)])

        

    def numIslands(self, grid: List[List[str]]) -> int:
        land_list={(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y]=="1"}
        result=0
        while(land_list):
            result +=1
            current=land_list.pop()
            self.dfs_solution(land_list,grid,current)
        return result