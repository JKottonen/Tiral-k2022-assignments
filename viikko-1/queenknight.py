from os import system
import os


def printMatrix(matrix: list):
    input("")
    os.system("cls")
    for line in matrix:
        print(line)
    print()

def possible_knight_positions(n, matrix, queenY, queenX):
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
            # (and two squares on X or Y axis, which doesn't matter because the queen makes them invalid anyways)
            if abs(queenY - y) <= 2 and abs(queenX - x) <= 2:
                continue

            matrix[y][x] = 2
            sum += 1
            #printMatrix(matrix)
            matrix[y][x] = 0
            
    return sum



def count(n: int):
    sum = 0
    matrix = [[0 for i in range(n)] for j in range(n)]
    queen = 1

    for y in range(n):
        for x in range(n):
            matrix[y][x] = queen
            sum += possible_knight_positions(n, matrix, y, x)
            matrix[y][x] = 0

    return sum


if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184