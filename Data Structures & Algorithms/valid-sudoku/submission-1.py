class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_dic=defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==".":
                    continue
                num=int(board[i][j])
                if num in my_dic.get(i,[]):
                    return False
                my_dic[i].append(num)
                if num in my_dic.get(9+j,[]):
                    return False
                my_dic[9+j].append(num)
                if num in my_dic.get((i//3,j//3),[]):
                    return False
                my_dic[(i//3,j//3)].append(num)
        return True     
                
                
