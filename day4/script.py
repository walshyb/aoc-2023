import re

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

result = 0
for line in lines:
    line = line.replace('\n', '')
    line = line.replace('  ', ' ')
    line = line.split(': ')[1]

    [winning_nums, my_nums] = line.split(' | ')
    winning_nums = set(winning_nums.split(' '))
    my_nums = set(my_nums.split(' '))
    matched_nums = list(winning_nums & my_nums)
    num_matched_nums = len(matched_nums) - 1
    
    if matched_nums:
        result += 2**num_matched_nums


print(result)

# right answer 28538 
