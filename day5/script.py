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



usable = None
for i in range(2, len(lines)):
    line = lines[i]
    if line == '\n':
        continue

    if 'seed-to-soil' in line:
        usable = seed_to_soil
        continue

    if 'soil-to-fertilizer' in line:
        usable = soil_to_fertilizer
        continue

    if 'fertilizer-to-water' in line:
        usable = fertilizer_to_water
        continue

    if 'fertilizer-to-water' in line:
        usable = fertilizer_to_water
        continue

    if 'water-to-light' in line:
        usable = water_to_light 
        continue

    if 'light-to-temp' in line:
        usable = light_to_temp 
        continue

    if 'temperature-to-humidity' in line:
        usable = temp_to_humidity 
        continue

    if 'humidity-to-location' in line:
        usable = humidity_to_location 
        continue

    [destination_range_start, source_range_start, range_length] = [int(item) for item in line.split(' ')]
    usable[range(source_range_start, source_range_start + range_length)] = (destination_range_start, source_range_start, range_length)


locations = []
for seed in seeds:
    soil = fetch(seed_to_soil, seed)
    fertilizer = fetch(soil_to_fertilizer, soil)
    water = fetch(fertilizer_to_water, fertilizer)
    light = fetch(water_to_light, water)
    temp = fetch(light_to_temp, light)
    humidity = fetch(temp_to_humidity, temp)
    location = fetch(humidity_to_location, humidity)

    locations.append(location)

print(min(locations))

# Result 218513636
