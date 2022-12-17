with open('input7.txt', 'r') as f:
    lines = f.read().splitlines()

current_work_directory = ""
file_size = 0
directory_file_sizes = {}
path = ""
dir_count = 0

for line in lines:
    if line == "$ cd ..":
        #print(f"Leaving {path}: {directory_file_sizes[path][current_work_directory]}")
        file_size2 = directory_file_sizes[path][current_work_directory]
        path = path[::-1]
        
        for i in range(len(path)):
            if path[i+1] == "/":
                path = path[i+1:]
                break
        
        if path == "/":
            current_work_directory = "/"
        else:
            for j in range(len(path)-1):
                if path[j+1] == "/":
                    current_work_directory = path[1:j+1]
                    break
        
        path = path[::-1]
        current_work_directory = current_work_directory[::-1]
        
        directory_file_sizes[path][current_work_directory] = directory_file_sizes[path][current_work_directory] + file_size2

        #print(f"Up {path}: {directory_file_sizes[path][current_work_directory]}")
    
    elif line[:4] == "$ cd":
        current_work_directory = line[5:]
        
        if path == "":
            path = current_work_directory
        else:
            path += current_work_directory + "/"
        
        file_size = 0
        dir_count = 0
    
    elif line == "$ ls":
        directory_file_sizes[path] = {current_work_directory: 0}
        #print(f"Listing {path}")
    
    elif line[:3] == "dir":
        dir_count += 1
    
    elif int(line[0]) in range(1,9):
        num = line.split()
        file_size = int(num[0])
        directory_file_sizes[path][current_work_directory] = directory_file_sizes[path][current_work_directory] + file_size


sum =0

for k, v in directory_file_sizes.items():
    for ke, va in v.items():
        #print(f"Path: {k} - {va}")
        if va <= 100000:
            sum += va
            print(f"Path: {k} - {va}")

print(f"\nSum: {sum}")


    


