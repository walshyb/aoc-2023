import re

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# Part 1
result = 0
for line in lines:
    nums = re.findall('\d', line)
    if not len(nums):
        continue

    first_num = nums[0]
    last_num = nums[-1]
    addition = first_num + last_num

    result += int(addition)

print("Part 1:" + str(result))


# Part 2
result = 0
for line in lines:
    num_map = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
            }
    pt1 = 0
    pt2 = 0

    nums = []
    while (pt1 < len(line)):
        running_str = line[pt1:pt2]
        found = num_map.get(running_str)
        if pt2 > len(line):
            pt1 += 1
            pt2 = pt1
            continue 

        if found:
            nums.append(found)
            pt1 = pt2 - 1
            pt2 = pt1
            continue

        if line[pt1].isnumeric():
            nums.append(line[pt1])
            pt1 += 1
            pt2 = pt1
            continue

        pt2 += 1


    first_num = nums[0]
    last_num = nums[-1]
    addition = first_num + last_num
    print(line, nums, addition)

    result += int(addition)

print(result)






