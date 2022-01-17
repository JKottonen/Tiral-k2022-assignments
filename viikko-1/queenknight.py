def possible_knight_positions(n, queenY, queenX):
    sum = 0
    for y in range(n):
        # Y axis not valid:
        if y == queenY:
            continue

        for x in range(n):
            # X axis not valid:
            if x == queenX:
                continue
            
            # Diagonal axis not valid:
            if x - y == queenX - queenY or x + y == queenX + queenY:
                continue
            
            # This one cover's the knights possible movements
            # (and two squares away on X or Y axis, which in this case doesn't matter because the queen makes them invalid anyways)
            if abs(queenY - y) <= 2 and abs(queenX - x) <= 2:
                continue
            
            # if knight's placement is valid, sum is added by 1
            sum += 1
            
    return sum

def count(n: int):
    sum = 0
    for y in range(n):
        for x in range(n):
            sum += possible_knight_positions(n, y, x)

    return sum


if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184