# Read input
filename = 'input.txt'
file = open(filename, 'r')
lines: list[str] = file.readlines()
file.close()

grid = []
neat_grid = []
start = None

# Build grid
for index, line in enumerate(lines):
    grid.append(list(line.strip()))
    neat_grid.append(list(line.strip()))

    if 'S' in line:
        start = (index, line.index('S'))


# in bound checker
def inbounds(row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def get_valid_positions(symbol, row, col):
    valid_positions = []
    if symbol == 'S':
        inbounds(row - 1, col) and grid[row-1][col] in ['7', '|', 'F'] and valid_positions.append((row - 1, col))
        inbounds(row + 1, col) and grid[row+1][col] in ['J', 'L', '|'] and valid_positions.append((row + 1, col))
        inbounds(row, col - 1) and grid[row][col-1] in ['L', '-', 'F'] and valid_positions.append((row, col - 1))
        inbounds(row, col + 1) and grid[row][col+1] in ['7', 'J', '-'] and valid_positions.append((row, col + 1))

    if symbol == '7':
        inbounds(row + 1, col) and grid[row+1][col] in ['|', 'J', 'S', 'L'] and valid_positions.append((row + 1, col))
        inbounds(row, col - 1) and grid[row][col-1] in ['-', 'S', 'L', 'F'] and valid_positions.append((row, col - 1))

    if symbol == 'J':
        inbounds(row - 1, col) and grid[row-1][col] in ['|', 'F', 'S', '7'] and valid_positions.append((row - 1, col))
        inbounds(row, col - 1) and grid[row][col-1] in ['-', 'S', 'F', 'L'] and valid_positions.append((row, col - 1))

    if symbol == 'L':
        inbounds(row - 1, col) and grid[row-1][col] in ['|', 'S', 'F', '7'] and valid_positions.append((row - 1, col))
        inbounds(row, col + 1) and grid[row][col+1] in ['-', 'J', 'S', '7'] and valid_positions.append((row, col + 1))

    if symbol == '|':
        inbounds(row - 1, col) and grid[row-1][col] in ['|', '7', 'S', 'F'] and valid_positions.append((row - 1, col))
        inbounds(row + 1, col) and grid[row+1][col] in ['|', 'J', 'S', 'L'] and valid_positions.append((row + 1, col))

    if symbol == '-':
        inbounds(row, col - 1) and grid[row][col-1] in ['-', 'F', 'S', 'L'] and valid_positions.append((row, col - 1))
        inbounds(row, col + 1) and grid[row][col+1] in ['-', 'J', 'S', '7'] and valid_positions.append((row, col + 1))

    if symbol == 'F':
        inbounds(row + 1, col) and grid[row+1][col] in ['|', 'J', 'S', 'L'] and valid_positions.append((row + 1, col))
        inbounds(row, col + 1) and grid[row][col+1] in ['-', 'J', 'S', '7'] and valid_positions.append((row, col + 1))

    return valid_positions



# (coords, steps from start)
nodes = [(start, 0)]
seen = set()
results = []
while nodes:
    [coords, steps_from_start] = nodes.pop(0)
    [row, col] = coords
    symbol = grid[row][col]

    neat_grid[row][col] = str(steps_from_start)

    seen.add(coords)
    valid_positions = get_valid_positions(symbol, row, col)
    #print(symbol, coords, valid_positions)

    results.append(steps_from_start)
    for position in valid_positions:
        if position in seen:
            print('what this value at', steps_from_start)
            print(position)
            continue

        nodes.append((position, steps_from_start+1))

result = 0
for row in neat_grid:
    for col in row:
        if col.isnumeric():
            result = max(int(col), result)

print(result)

if filename == 'input.sample':
    print('-------------')

    for row in neat_grid:
        for col in row:
            print(col, end=' ')
        print('')

    print('-------------')

    for row in grid:
        for col in row:
            print(col, end=' ')
        print('')
        

if filename == 'input.txt':
    file = open('out.txt', 'w')
    for row in neat_grid:
        for col in row:
            while len(col) < 4:
                col = ' ' + col
            file.write(col + ' ')
        file.write('\n')
    file.close()


# 7088 too low
