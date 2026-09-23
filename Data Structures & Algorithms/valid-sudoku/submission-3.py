class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # CHANGE 1:
        # Use sets instead of lists because membership lookup is O(1) average.
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):

                value = board[i][j]

                if value == ".":
                    continue

                # CHANGE 2:
                # No need to convert to int; the character itself is enough.
                box_key = (i // 3, j // 3)

                # CHANGE 3:
                # Keep row, column, and box state separate.
                # This is clearer than mixing them into one dictionary.
                if (
                    value in rows[i]
                    or value in cols[j]
                    or value in boxes[box_key]
                ):
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxes[box_key].add(value)

        return True   
                
                
