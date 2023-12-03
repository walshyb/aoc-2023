import re

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# Part 1
result = 0
cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
for line in lines:
    game_id = int(re.findall('Game (\d+):', line)[0])
    game_possible = True

    # Make list of cubes (i.e. [3 blue, 4 red, 1 red])
    pulled_cubes = re.split(': |; |, ', line)

    # Remove first item (Game X: )
    pulled_cubes.pop(0)

    for pulled_cube_info in pulled_cubes:
        [num_cubes, color] = pulled_cube_info.strip().split(' ')
        num_cubes = int(num_cubes)

        if num_cubes > cubes[color]:
            game_possible = False
            break

    if game_possible:
        result += game_id

print('Part 1: ' + str(result))


# Part 2

result = 0
for line in lines:
    # Make list of cubes (i.e. [3 blue, 4 red, 1 red])
    pulled_cubes = re.split(': |; |, ', line)
    # Remove first item (Game X: )
    pulled_cubes.pop(0)
    
    min_cubes = {
        'red': 0,
        'blue': 0,
        'green': 0 
    }

    for pulled_cube_info in pulled_cubes:
        [num_cubes, color] = pulled_cube_info.strip().split(' ')
        num_cubes = int(num_cubes)

        min_cubes[color] = max(num_cubes, min_cubes[color])

    power = min_cubes['red'] * min_cubes['blue'] * min_cubes['green']

    result += power

print('Part 2: '+ str(result))

# Too lower: 3557
