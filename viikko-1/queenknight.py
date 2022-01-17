from logging.handlers import QueueListener


def printMatrix(matrix: list):
    for line in matrix:
        print(line)
    

def count(n: int):
    matrix = [[0 for i in range(n)] for j in range(n)]
    queen = 1
    knight = 2
    matrix[1][0] = queen
    matrix[3][3] = knight
    printMatrix(matrix)

if __name__ == "__main__":
#    print(count(3)) # 0
    print(count(4)) # 40
#    print(count(5)) # 184