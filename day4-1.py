import numpy as np

file = 'day4.txt'
word = 'XMAS'
directions = {(-1, -1), (-1, 0), (0, -1), (-1, 1), (0, 1), (1, 0), (1, -1), ( 1, 1)}

def parse_input(file):
    grid = []
    with open(file) as text:
        for line in text:
            grid.append([char for char in line.strip('\n')])
        print(len(grid[0]), len(grid))
        return grid

def is_valid_position(x, y):
    if x < 0 or x >= len(grid[0]):
        return False
    if y < 0 or y >= len(grid):
        return False
    return True

def find_first_char(grid):
    np_grid = np.array(grid)
    x_positions = np.where(np_grid == word[0])
    return list(zip(x_positions[0], x_positions[1]))

def find_directions(first_char_coords: list[tuple[int, int]]):
    promising_starts = []
    for direction in directions:
        dx, dy = direction
        for coords in first_char_coords:
            x, y = coords
            x_to_check, y_to_check = (x + dx, y + dy)
            if not is_valid_position(x_to_check, y_to_check):
                continue
            if grid[x_to_check][y_to_check] != word[1]:
                continue
            promising_starts.append({
                'start': coords,
                'direction': direction
                })
    print(promising_starts)
    return promising_starts

def count_occurences(promising_starts):
    occurences = 0
    valid_paths = []
    for start in promising_starts:
        position = start['start']
        direction = start['direction']
        start['path'] = []
        valid = True
        for i in range(1, len(word)):
            next_pos = (position[0] + (direction[0] * i), position[1] + (direction[1] * i))
            if not is_valid_position(next_pos[0], next_pos[1]):
                valid = False
                break
            if grid[next_pos[0]][next_pos[1]] != word[i]:
                valid = False
                break
            else:
                start['path'].append(next_pos)
        if valid: 
            occurences += 1
            valid_paths.append(start)
    print(f'{occurences = }')
    return valid_paths

grid = parse_input(file)
for row in grid:
    print(row)
first_chars = find_first_char(grid)
print(first_chars)
promising_starts = find_directions(first_chars)
valid_paths = count_occurences(promising_starts)
# print(valid_paths)