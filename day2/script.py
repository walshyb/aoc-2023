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

print(result)





    



