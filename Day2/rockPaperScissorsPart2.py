strategy_guide = open("input2.txt", "r")

shape_points = {'A': 1, 'B': 2, 'C': 3}
round_points = {'win': 6, 'lose': 0, 'draw': 3}
lose_points = {'A': 3, 'B': 1, 'C': 2}
win_points = {'A': 2, 'B': 3, 'C': 1}

lines = [line.split() for line in strategy_guide]

point_total = 0
round_num = 0

for line in lines:
    round_num += 1
    if line[1] == 'X':
        point_total += lose_points[line[0]] + round_points['lose']
    elif line[1] == 'Y':
        point_total += shape_points[line[0]] + round_points['draw']
    else:
        point_total += win_points[line[0]] + round_points['win']

strategy_guide.close()

print(f"Rounds: {round_num} \nPoints: {point_total}")
