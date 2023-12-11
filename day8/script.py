# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

sequence = lines[0]

nodes = {}
for i in range(2, len(lines)):
    line = lines[i]
    key = line.split(' =')[0]
    left = line.split('(')[1].split(',')[0]
    right = line.split(', ')[1].split(')')[0]

    nodes[key] = (left, right)

steps = 0
current = 'AAA'

while True:
    index = steps % (len(sequence) - 1)
    current_sequence_item = sequence[index]
    #print(index, steps, current_sequence_item)
    if current == 'ZZZ':
        print(steps)
        break

    [left, right] = nodes[current]
    #print(current, left, right, current_sequence_item)

    if current_sequence_item == 'L':
        current = left
    else:
        current = right

    steps += 1



# too low 11609
# right 12643
