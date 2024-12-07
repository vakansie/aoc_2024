file = r'day6.txt'

def parse_input(file):
    grid = []
    with open(file) as text:
        for r_index, line in enumerate(text):
            row = []
            for column, char in enumerate(line):
                if char == '.':
                    row.append(0)
                elif char == '^':
                    row.append(0)
                    start = (r_index, column)
                elif char == '#':
                    row.append(1)
            grid.append(row)
    return start, grid

def is_on_the_map(x, y):
    if x < 0 or x >= len(grid[0]):
        return False
    if y < 0 or y >= len(grid):
        return False
    return True

def walk_grid(grid, start_position):
    direction_loop = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    print(f'{start_position = }')
    path = [start_position]
    position = start_position
    on_the_map = True
    while on_the_map:
        next_pos = tuple(map(sum, zip(position, direction_loop[direction_index])))
        on_the_map = is_on_the_map(next_pos[0], next_pos[1])
        if on_the_map:
            x, y = next_pos
            if grid[x][y]:
                direction_index = (direction_index + 1) % 4
            else:
                position = next_pos
                path.append(position)
        elif not on_the_map: print(f'left the map: {next_pos}')
    return path

start, grid = parse_input(file)
# for row in grid:
#     print(row)
path = walk_grid(grid, start)
# for x, row in enumerate(grid):
#     for y, char in enumerate(row):
#         print('X' if (x, y) in path else char, end=' ')
#     print()
print(path)
print(f'positions visited: {len(path)}')
print(f'unique positions visited: {len(list(set(path)))}')
print(len(grid[0]), len(grid))