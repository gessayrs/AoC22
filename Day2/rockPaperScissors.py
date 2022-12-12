strategy_guide = open("input2.txt", "r")

shape_points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
round_points = {'win': 6, 'lose': 0, 'draw': 3}

point_total = 0
round_num = 0

for line in strategy_guide:
    rps_round = line.split()
    shape_point = []
    round_num += 1
    
    for i in rps_round:
        shape_point.append(shape_points[i])

    if shape_point[0]==1 and shape_point[1]==3:
        point_total += round_points['lose'] + shape_point[1]
    elif shape_point[0]==3 and shape_point[1]==1:
        point_total += round_points['win'] + shape_point[1]
    elif shape_point[0] < shape_point[1]:
        point_total += round_points['win'] + shape_point[1]
    elif shape_point[0] > shape_point[1]:
        point_total += round_points['lose'] + shape_point[1]
    else:
        point_total += round_points['draw'] + shape_point[1]

strategy_guide.close()

print(f"Rounds: {round_num} \nPoints: {point_total}")
