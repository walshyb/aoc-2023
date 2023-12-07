# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_humidity = {}
humidity_to_location = {}

soil_to_seed = {}
fertilizier_to_soil = {}
water_to_fertilizer = {}
light_to_water = {}
temp_to_light = {}
humidity_to_temp = {}
location_to_humidity = {}

seeds_raw = lines[0].split(': ')[1].split(' ')
seeds = [int(seed) for seed in seeds_raw ]

def fetch(dataset, value):
    result = { dataset[key] for key in dataset if value in key }
    if not len(result):
        return value

    result = result.pop()
    [destination_range_start, source_range_start, range_length] = result

    diff = value - source_range_start

    return destination_range_start + diff


def reverse_fetch(dataset, value):
    result = { dataset[key] for key in dataset if value in key }
    if not len(result):
        return value

    result = result.pop()
    [destination_range_start, source_range_start, range_length] = result

    diff = value - destination_range_start

    return source_range_start + diff


usable = None
reverse = None
for i in range(2, len(lines)):
    line = lines[i]
    if line == '\n':
        continue

    if 'seed-to-soil' in line:
        usable = seed_to_soil
        reverse = soil_to_seed
        continue

    if 'soil-to-fertilizer' in line:
        usable = soil_to_fertilizer
        reverse = fertilizier_to_soil 
        continue

    if 'fertilizer-to-water' in line:
        usable = fertilizer_to_water
        reverse = water_to_fertilizer 
        continue

    if 'water-to-light' in line:
        usable = water_to_light 
        reverse = light_to_water 
        continue

    if 'light-to-temp' in line:
        usable = light_to_temp 
        reverse = temp_to_light 
        continue

    if 'temperature-to-humidity' in line:
        usable = temp_to_humidity 
        reverse = humidity_to_temp 
        continue

    if 'humidity-to-location' in line:
        usable = humidity_to_location 
        reverse = location_to_humidity
        continue

    [destination_range_start, source_range_start, range_length] = [int(item) for item in line.split(' ')]
    usable[range(source_range_start, source_range_start + range_length)] = (destination_range_start, source_range_start, range_length)
    reverse[range(destination_range_start, destination_range_start + range_length)] = (destination_range_start, source_range_start, range_length)


def run_it(seed):
    soil = fetch(seed_to_soil, seed)
    fertilizer = fetch(soil_to_fertilizer, soil)
    water = fetch(fertilizer_to_water, fertilizer)
    light = fetch(water_to_light, water)
    temp = fetch(light_to_temp, light)
    humidity = fetch(temp_to_humidity, temp)
    location = fetch(humidity_to_location, humidity)

    return location


def part_1():
    locations = []
    for seed in seeds:
        location = run_it(seed)
        locations.append(location)

    #print(min(locations))

    # Result 218513636

part_1()

def part_2():
    ranges = []
    min_location = float('inf')

    for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]): 
        ranges.append(range(seed_start, seed_start + seed_range))


    def reverse_run_it(location):
        humidity = reverse_fetch(location_to_humidity, location)
        temp = reverse_fetch(humidity_to_temp, humidity)
        light = reverse_fetch(temp_to_light, temp)
        water = reverse_fetch(light_to_water, light)
        fertilizer = reverse_fetch(water_to_fertilizer, water)
        soil = reverse_fetch(fertilizier_to_soil, fertilizer)
        seed = reverse_fetch(soil_to_seed, soil)

        return seed


    location = 0
    lowest_location = float('inf')
    # Reverse lookup
    while True:
        seed = reverse_run_it(location)

        if True in { ranges[key] for key in ranges if seed in key }:
            lowest_location = location
            break

        if lowest_location != float('inf'):
            break

        location += 1

    print(lowest_location)


part_2()
# too high 280278922
# too high 550136751
# right answer: 81956384
