"""
1. plot all the x,y points across the snakes
2. id all the intersections
3. calculate the mahattan distance for each
4. find the min
"""

# get the 2 lines of input
input_file = "2019/3/input.a"
# input_file = "2019/3/test2.a"; print("running using a test input file")
# input_file = "2019/3/test0"; print("running using a test input file")
line1_moves, line2_moves = (x.strip() for x in open(input_file).readlines())
print("input lines:")
print(line1_moves)
print(line1_moves)

def derive_plots(start_xy, direction_move, start_index):
    direction = direction_move[0]
    move = int(direction_move[1:])
    start_x, start_y = start_xy

    if direction in ["R", "U"]:
        range_increment = 1
    else:
        range_increment = -1

    if direction in ["L", "R"]:
        # derive points on x axis, y axis constant
        plots = {}
        for idx, x in enumerate(range(start_x, start_x + move * range_increment + range_increment, range_increment), start=start_index):
            if idx != 0:  # skip first plot
                plots[idx] = (x, start_y)
    else:
        # derive points on y axis, x axis constant
        plots = {}
        for idx, y in enumerate(range(start_y, start_y + move * range_increment + range_increment, range_increment), start=start_index):
            if idx != 0:  # skip first plot
                plots[idx] = (start_x, y)

    return plots


line1 = {}
max_key = 0
end_point = (0, 0)
line1[max_key] = end_point  # seed starting plot
for direction_move in line1_moves.split(","):
    plots = derive_plots(end_point, direction_move, max_key)
    max_key = max(plots.keys())
    end_point = plots[max_key]
    line1 = {**line1, **plots}

line2 = {}
max_key = 0
end_point = (0,0)
line2[max_key] = end_point  # seed starting point
for direction_move in line2_moves.split(","):
    plots = derive_plots(end_point, direction_move, max_key)
    max_key = max(plots.keys())
    end_point = plots[max_key]
    line2 = {**line2, **plots}

intersections = set(line1.values()) & set(line2.values())

min_distance = min(abs(x) + abs(y) for x, y in intersections if (x, y) != (0,0))

print("question a", min_distance)  # 709

# lookup the steps in the dict using the values of the intersections
# then get the min combined number of steps
min_steps = min(
    list(line1.values()).index(t) +
    list(line2.values()).index(t)
    for t in intersections
    if t != (0,0)
)

print("question b", min_steps)

pass