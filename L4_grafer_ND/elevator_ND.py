

def find(f, s, g, u, d):
    if s == g:
        return 0
    elif s-d < f and s+u > f:
        return -90000000
    else:
        return min(find(f, s+u, g, u, d), find(f, s-d, g, u, d)) + 1


# print(find(20, 10, 15, 1, 1))


def stelevator(floors, start, goal, up, down):
    going_up = start < goal
    going_down = start > goal
    destintion_reached = start == goal
    print(f"Floors {floors}, start {start}, gloal {goal} ")
    if goal > floors or goal < 1:
        raise Exception("Not possible")
    elif going_up:
        if start + up - down > goal:
            raise Exception("Not possible")
        return stelevator(floors, start + up, goal, up, down) + 1
    elif going_down:
        if start - down + up < goal:
            raise Exception("Not possible")
        return stelevator(floors, start - down, goal, up, down) + 1
    elif destintion_reached:
        return 1


#print(stelevator(15, 2, 13, 4, 2))


def mad_elevator(floors, start, goal, up, down):
    print(f"Floors {floors}, start {start}, gloal {goal} ")
    if goal > floors or goal < 1:
        return 0
    elif start == goal:
        return 1
    elif start + up > goal and start + up - down < goal:
        return 0
    elif start + up > floors:
        return mad_elevator(floors, start-down, goal, up, down)
    elif start - down < 0:
        return mad_elevator(floors, start+up, goal, up, down)
    else:
        return min(mad_elevator(floors, start+up, goal, up, down), mad_elevator(floors, start-down, goal, up, down))


print(str(mad_elevator(10, 2, 8, 1, 2)))