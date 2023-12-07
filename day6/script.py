# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

parsed_times = lines[0].split(' ')
parsed_distances  = lines[1].split(' ')

times = [int(line) for line in parsed_times]
distances = [int(line) for line in parsed_distances]

def race(speed, remaining_time, distance):
    return speed * remaining_time > distance


result = 1

for index in range(len(times)):
    time = times[index]
    distance = distances[index]

    num_ways_to_beat_record = 0
    beat = False

    for counter in range(time):
        wins_race = race(counter, time - counter, distance)

        if wins_race:
            beat = True
            num_ways_to_beat_record += 1

        if beat and not wins_race:
            break


    result *= num_ways_to_beat_record

print(result)
# Result: 316800

