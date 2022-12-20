with open('input7.txt', 'r') as f:
    lines = f.read().splitlines()

file_size = 0
directory_file_sizes = {}
path = ""
total = 0

for line in lines:
    if line == "$ cd ..":
        path = path[::-1]
        
        for i in range(len(path)-1):
            if path[i+1] == "/":
                path = path[i+1:]
                break

        path = path[::-1]
    
    elif line[:4] == "$ cd":
        if line[5:] == "/":
            path = "/"
        else:
            path += line[5:] + "/"

        file_size = 0
    
    elif line == "$ ls":
        directory_file_sizes[path] = 0
    
    elif line[:3] == "dir":
        pass
    
    elif int(line[0]) in range(1,10):
        num = line.split()
        file_size = int(num[0])
        directory_file_sizes[path] = directory_file_sizes[path] + file_size


for k, v in directory_file_sizes.items():
    path_size = len(k)
    k_reverse = k[::-1]

    for i in range(1, len(k_reverse)):
        if k_reverse[i] == "/":
            directory_file_sizes[k[:path_size-i]] += directory_file_sizes[k]


total = 30000000 - (70000000 - directory_file_sizes["/"])

directory_values = []

for k, v in directory_file_sizes.items():
    if v >= total:
        directory_values.append(v)

directory_values.sort()

print(f"Smallest Directory to Delete - {directory_values[0]}")
