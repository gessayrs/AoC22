calories = open("input.txt", "r")
#print(calories.read())

total_cals = []
num = 0

for food in calories:
    if food != "\n":
        num += int(food)
    else:
        total_cals.append(num)
        num = 0

total_cals.sort(reverse=True)
#print(total_cals)

top_three = 0

for cals in total_cals[:3]:
    top_three += cals

print(top_three)
