from collections import defaultdict 

# Read input
file = open('input.txt', 'r')
lines: list[str] = file.readlines()
file.close()

# Part 1
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


print('part 1', result)

# right answer 28538 

# Part 2
result = 0

instances = defaultdict(int) 


for card_num in range(1, len(lines) + 1):
    instances[card_num] += 1

    while instances[card_num] and card_num != len(lines) + 1:
        result += 1
        line = lines[card_num-1]
        line = line.replace('\n', '')
        line = line.replace('  ', ' ')

        [winning_nums, my_nums] = line.split(' | ')
        winning_nums = set(winning_nums.split(' '))
        my_nums = set(my_nums.split(' '))
        matched_nums = list(winning_nums & my_nums)
        num_matched_nums = len(matched_nums)

        for i in range(card_num+1, card_num + 1 + num_matched_nums):
            instances[i] += 1

        instances[card_num] -= 1


print('part 2', result)

# Right answer 9425061
