with open('input4.txt', 'r') as f:
    lines = f.read().splitlines()

total_pairs = 0

for line in lines:
    nums = []
    remove_comma = line.split(',')
    
    for i in range(len(remove_comma)):
        nums.append(remove_comma[i].split('-'))
    
    if (int(nums[0][0]) <= int(nums[1][0])) and (int(nums[0][1]) >= int(nums[1][1])):
        total_pairs += 1
    elif (int(nums[0][0]) >= int(nums[1][0])) and (int(nums[0][1]) <= int(nums[1][1])):
        total_pairs += 1

print(f"Total assignment pairs: {total_pairs}")
