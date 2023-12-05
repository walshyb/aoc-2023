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

    print(min(locations))

    # Result 218513636

#part_1()


    

def part_2():
    ranges = []
    min_location = float('inf')

    for seed_start, seed_range in zip(seeds[0::2], seeds[1::2]): 
        ranges.append(range(seed_start, seed_start + seed_range))

    for seed_range in ranges:
        # Binary search!!!
        # that's the key to it all
        # i missed the trick in pt 1
        # but we got it now

        #for seed in seed_range:
        #    min_location = min(min_location, run_it(seed))

        local_min = run_it(seed_range[0])
        left_ptr = 0
        right_ptr = len(seed_range) - 1
        
        while left_ptr < right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            candidate1 = run_it(seed_range[mid_ptr])
            candidate2 = run_it(seed_range[mid_ptr + 1])

            #print(seed_range[left_ptr], seed_range[mid_ptr], seed_range[right_ptr])
            candidate3 = run_it(seed_range[right_ptr])
            candidate4 = run_it(seed_range[left_ptr])
            print(candidate4, candidate1, candidate3)

            if candidate1 > candidate2:
                print('go left')
                left_ptr = mid_ptr + 1
            else:
                print('go right')
                right_ptr = mid_ptr
        
            local_min = min(local_min, candidate1, candidate2, candidate3, candidate4)

        min_location = min(min_location, local_min)

        break

    print(min_location)


part_2()
# too high 280278922
# too high 550136751
