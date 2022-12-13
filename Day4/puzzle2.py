with open('input4.txt', 'r') as f:
    lines = f.read().splitlines()

total_pairs = 0

for line in lines:
    nums = []
    first_range = []
    second_range = []
    remove_comma = line.split(',')
    
    for i in range(len(remove_comma)):
        nums.append(remove_comma[i].split('-'))
    
    for num in range(int(nums[0][0]), int(nums[0][1])+1):
        first_range.append(num)
    
    for num in range(int(nums[1][0]), int(nums[1][1])+1):
        second_range.append(num)

    for num in first_range:
        if num in second_range:
            total_pairs += 1
            break

print(f"Total assignment pairs: {total_pairs}")
