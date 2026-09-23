class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=defaultdict(list)
        raw=defaultdict(list)
        box=defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[i])):
                s=board[i][j]
                if s==".":
                    continue
                num=int(s)
                if num in col.get(i,[]):
                    return False
                col[i].append(num)
                if num in raw.get(j,[]):
                    return False
                raw[j].append(num)
                if num in box.get((i//3,j//3),[]):
                    return False
                box[(i//3,j//3)].append(num)
        return True     
                
                
