# Read input
filename = 'input.sample'
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



# (coords, steps from start, path of coords to get there)
nodes = [(start, 0, [])]
seen = set()
loop_path = None

# Get loop path
while nodes:
    [coords, steps_from_start, path] = nodes.pop()
    [row, col] = coords
    symbol = grid[row][col]

    if path and coords == path[0]:
        loop_path = path
        break

    valid_positions = get_valid_positions(symbol, row, col)

    for position in valid_positions:
        if position in seen:
            continue
        seen.add(position)
        path.append(position)
        nodes.append((position, steps_from_start+1, path))

# Define loop bounds
# Probs not needed
for coord in loop_path:
    neat_grid[coord[0]][coord[1]] = '@'

seen = set()
running_path = []
friendly_parts = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) in seen:
            continue

        nodes = [(i,j)]
        good = True
        local_seen = set()
        while nodes:
            current = nodes.pop()
            [row, col] = current

            if current in local_seen or neat_grid[row][col] == '@' or neat_grid[row][col] == 'I':
                continue
        
            local_seen.add(current)

            # Add neighbors
            neighbors = [(row-1,col-1), (row-1,col),(row-1,col+1), (row, col-1), (row, col+1), (row+1,col-1), (row+1, col), (row+1,col+1)]
            #neighbors = [(row-1,col),(row, col-1), (row, col+1),(row+1, col)]

            for neighbor in neighbors:
                [neighbor_row, neighbor_col] = neighbor
                if not inbounds(neighbor_row, neighbor_col):
                    good = False
                    seen.add(neighbor)
                    break

                #if neat_grid[neighbor_row][neighbor_col] == '.':
                if neighbor not in loop_path and neighbor not in local_seen:
                    nodes.append(neighbor)
                    

            if good == False:
                break

        if good:
            for coord in local_seen:
                neat_grid[coord[0]][coord[1]] = 'I'
            friendly_parts = friendly_parts.union(local_seen)

            




print(len(friendly_parts))
chars = {'F': '╔', '7': '╗', 'L': '╚', 'J': '╝', '-': '═', '|': '║', 'S': '@', '.': '.'}

if filename == 'input.sample':
    print('-------------')

    for row in neat_grid:
        for col in row:
            print(chars[col], end=' ')
        print('')

    print('-------------')

    for row in grid:
        for col in row:
            print(chars[col], end=' ')
        print('')
        

if filename == 'input.txt':
    file = open('out2.txt', 'w')
    for row in neat_grid:
        for col in row:
            while len(col) < 4:
                col = ' ' + col
            file.write(col + ' ')
        file.write('\n')
    file.close()


# 4633 too high

