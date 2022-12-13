with open('input5.txt', 'r') as f:
    lines = f.read().splitlines()

stacks = [
    ['Z', 'J', 'G'],
    ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
    ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
    ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
    ['G', 'C', 'F', 'S', 'V', 'Q'],
    ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
    ['H', 'F', 'S', 'B', 'V'],
    ['F', 'J', 'Z', 'S'],
    ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
]

for line in lines:
    instructions = line.split()
    num_crates = int(instructions[1])
    from_stack = int(instructions[3])
    to_stack = int(instructions[5]) 

    for crate in range(num_crates):
        popped = stacks[from_stack -1].pop()
        stacks[to_stack -1].append(popped)

top_stack = ""

for stack in stacks:
    top_stack += stack[-1]

print(f"Crates on top: {top_stack}")
