# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

time = int(''.join(lines[0].replace(' ', '')))
distance  = int(''.join(lines[1].strip().replace(' ', '')))

def race(speed, remaining_time, distance):
    return speed * remaining_time > distance

result = 0
beat = False

for counter in range(time):
    wins_race = race(counter, time - counter, distance)

    if wins_race:
        beat = True
        result += 1

    if beat and not wins_race:
        break

print(result)
# Result: 316800

