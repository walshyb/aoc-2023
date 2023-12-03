# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

grid = [list(line.strip()) for _, line in enumerate(lines) ]
rows = len(grid)
columns = len(grid[0])

# Approach start at row 1 (not 0)
# Look for symbols (non digits, non-periods)
# Look in all directions for digit
# Do left and right search to get full number
# Save partnumber
# Save coords of that number

part_numbers = []
seen_coords = set()

def is_symbol(char):
    return not char.isnumeric() and char != '.'

def inbounds(row = 0, col = 0):
    return row >= 0 and row < rows and col >= 0 and col < columns

def save_partnumber(row, col):
    if (row, col) in seen_coords:
        return

    # Go left until can't go any farther
    # Go right until we hit .
    running_partnumber = '';
    while cell(row,col-1).isnumeric():
        col -= 1

    while cell(row,col).isnumeric():
        running_partnumber += cell(row, col)
        seen_coords.add((row, col))
        col += 1

    part_numbers.append(int(running_partnumber))

# Returns cell item or empty string
def cell(row, col):
    return (inbounds(row, col) and grid[row][col]) or ''

    
def peek_around(row, col):
    # Up-right
    if cell(row-1, col+1).isnumeric():
        save_partnumber(row-1, col+1)

    # Up-left
    if cell(row-1, col-1).isnumeric():
        save_partnumber(row-1, col-1)
    
    # Down left
    if cell(row+1, col-1).isnumeric():
        save_partnumber(row+1, col-1)

    # Down right
    if cell(row+1, col+1).isnumeric():
        save_partnumber(row+1, col+1)

    # Right
    if cell(row, col+1).isnumeric():
        save_partnumber(row, col+1)

    # Left
    if cell(row, col-1).isnumeric():
        save_partnumber(row, col-1)

    # Up 
    if cell(row-1, col).isnumeric():
        save_partnumber(row-1, col)

    # Down 
    if cell(row+1, col).isnumeric():
        save_partnumber(row+1, col)

# Part 1
for i in range(rows):
    for j in range(1, columns):
        current_char = grid[i][j]
        
        if is_symbol(current_char):
            peek_around(i,j)


print(sum(part_numbers))

# 535351 right answer
