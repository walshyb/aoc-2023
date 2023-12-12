# Read input
file = open('input.sample2', 'r')
lines: list[str] = file.readlines()
file.close()

sequence = lines[0]

nodes = {}
current_batch = []

for i in range(2, len(lines)):
    line = lines[i]
    key = line.split(' =')[0]
    left = line.split('(')[1].split(',')[0]
    right = line.split(', ')[1].split(')')[0]

    if key[-1] == 'A':
        current_batch.append(key)

    nodes[key] = (left, right)


def do_all_end_with_z():
    for item in current_batch:
        if item[-1] != 'Z':
            return False
    return True

steps = 0
while True:
    print(current_batch)
    if do_all_end_with_z():
        break

    next_batch = []
    index = steps % (len(sequence) - 1)
    current_sequence_item = sequence[index]

    for current_key in current_batch:
        [left, right] = nodes[current_key]

        if current_sequence_item == 'L':
            next_batch.append(left)
        else:
            next_batch.append(right)

    current_batch = next_batch
    steps += 1



print(steps)

# 100068 too low
# 100069 too low
