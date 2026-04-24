def furthestDistanceFromOrigin(moves: str) -> int:
    count = 0
    count2 = 0
    for move in moves:
        if move == "L":
            count += 1
        elif move == "R":
            count2 += 1

    if count > count2:
        moves = moves.replace("_", "L")
    elif count2 > count:
        moves = moves.replace("_", "R")
    elif count == count2:
        moves = moves.replace("_", "L")
    print(moves)
    count = 0
    for move in moves:
        if move == "L":
            count -= 1
        elif move == "R":
            count += 1

    return abs(count)

moves = "_R"
print(furthestDistanceFromOrigin(moves))



# second solution
def farthestDistanceFromOrigin(moves: str):
    Distance = moves.count("R") - moves.count("L")
    wildcard = moves.count("_")
    return abs(Distance) + wildcard

moves = "_R"
print(farthestDistanceFromOrigin(moves))




        