from typing import List, Union

def return_board(grid_size: List[int], mine_locations: List[List[str]]) -> List[List[str]]: # grid_size: [col, row]
    board_ans = grid_size.copy()
    row = grid_size[1]
    col = grid_size[0]
    for r in range(row):
        for c in range(col):
            board_ans[r][c] = find_neighbour(mine_locations, row, col)

    return board_ans

def find_neighbour(mine_locations: List[List[str]], row: int, col: int) -> Union[int, str]:
    first_row_length = len(mine_locations)
    col_length = len(mine_locations[0])
    for lst in mine_locations:
        if len(lst) != first_row_length:
            raise ValueError('mine_locations must have same row lengths')
    if row > first_row_length or row < 0:
        raise ValueError(f'row index out of bounds: {row}')
    if col > col_length or col < 0:
        raise ValueError(f'col index out of bounds: {col}')
    
    if mine_locations[row][col] == '*':
        return '*'

    ans = 0
    DIRS = [(1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    
    for dir in DIRS:
        new_row = row + dir[0]
        new_col = col + dir[1]
        is_in_grid = new_row > -1 and new_row < first_row_length and new_col > -1 and new_col < col_length
        if is_in_grid and mine_locations[new_row][new_col] == '*':
            ans += 1

    if ans == 0:
        ans = '.'

    return ans