with open('input7.txt', 'r') as f:
    lines = f.read().splitlines()

tree_level = 0
current_work_directory = ""
#previous_directory = ""
#first_level_directory = []
file_size = 0
directory_file_sizes = {}
#count =0

for line in lines:
    if line == "$ cd ..":
        #print(f"CWD: {previous_directory}")
        tree_level -=1
        print(f"Up One Level: {tree_level}")
        if file_size <=100000:
            directory_file_sizes[current_work_directory] = file_size
        #print(directory_file_sizes)
        file_size =0
        #count +=1
    elif line[:4] == "$ cd":
        if file_size <=100000:
            directory_file_sizes[current_work_directory] = file_size
        current_work_directory = line[5:]
        print(f"File Size of {current_work_directory}: {file_size}")
        print(f"CWD: {line[5:]}")
        #previous_directory = current_work_directory
        tree_level +=1
        print(f"Level: {tree_level}")
        file_size =0
    elif line == "$ ls":
        print(f"Listing: {current_work_directory}")
    elif line[:3] == "dir":
        print(f"\tDirectory: {line[4:]}")
    elif int(line[0]) in range(1,9):
        print(f"\tFile: {line}")
        num = line.split()
        file_size += int(num[0])

print("\n")
for k,v in directory_file_sizes.items():
    print(f"Dir: {k} - {v}")

sum = 0
for value in directory_file_sizes.values():
    sum += value
print(f"\nSum: {sum}")


    


