
def puzzle(a):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(n):
        if grid[row][x] == num:
            return False

    for x in range(n):
        if grid[x][col] == num:
            return False

    if n==4:
        startRow=row - row % 2
        startCol=col - col % 2
        for i in range(2):
            for j in range(2):
                if grid[i+startRow][j + startCol]==num:
                    return False
    if n==6:
        startRow=row - row % 2
        startCol=col - col % 3
        for i in range(2):
            for j in range(3):
                if grid[i+startRow][j + startCol]==num:
                    return False

    if n==8:
        startRow=row - row % 2
        startCol=col - col % 4
        for i in range(2):
            for j in range(4):
                if grid[i+startRow][j + startCol]==num:
                    return False

    if n==9:
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
    return True


def Suduko(grid, row, col):
    if (row == n - 1 and col == n):
        return True
    if col == n:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, n + 1, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

n=int(input("enter grid of sudoko: "))
grid = []
print("enter numbers :")
for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input()))
    grid.append(b)

print("------Problem sudoku matrix------- ")
for i in range(n):
    for j in range(n):
        print(grid[i][j],end=" ")
    print()

print("-------Solution Sudoku Matrix-------")
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")