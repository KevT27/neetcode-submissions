from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(list)
        columns = defaultdict(list)

        groups = defaultdict(list)

        group = 0

        for i, row in enumerate(board):

            for k, item in enumerate(row):
                
                group = (i // 3) * 3 + (k // 3)

                if item in rows[i] and item.isdigit():
                    print(f"Duplicated {item} in Row {i}")
                    return False
                else:
                    rows[i].append(item)    # Add to Current Row

                if item in columns[k] and item.isdigit():
                    print(f"Duplicated {item} in Column {k}")
                    return False
                else:
                    columns[k].append(item) # Add to Current Column

                if item in groups[group] and item.isdigit():
                    return False
                else:
                    groups[group].append(item)
                

        return True