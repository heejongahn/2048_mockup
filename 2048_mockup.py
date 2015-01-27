import random
from termcolor import colored

# 2048 Mockup in Python3 : Made by Heejong Ahn


class Table():


    # function __init__
    # Initializes the game: Print instructions. Make a game table and print it

    def __init__(self):

        print (' = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
        print ('|| Python3 version of 2048, made by << Heejong Ahn >>      ||')
        print ('|| Please enjoy, and let me know if you find errors.       ||')
        print ('|| You can check the full code at github.com/heejongahn    ||')
        print (' = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
        print ('\n')

        self.size = int(input('Size of the table? '))
        self.table = self.makeTable()
        self.freeList = list(range(1,self.size*self.size))
        self.point = 0
        self.maxValue = 2
        self.colorMap = {'-': 'white', 2:'white', 4: 'white', 8: 'yellow',
                16: 'yellow', 32: 'green', 64: 'green', 128: 'cyan',
                256: 'blue', 512: 'magenta', 1024: 'red', 2048: 'grey'}

        self.printTable()

    # function makeTable
    # Makes a size*size size game table and return it

    def makeTable(self):
        size = self.size

        table = [0] * size
        for i in range(size):
            table[i] = ['-'] * size
        table[0][0] = 2
        return table

    # function printTable
    # Prints current game table state

    def printTable(self):
        table = self.table
        colorMap = self.colorMap

        for line in table:
            for e in line:
                val = str(e)
                blank = " " * (4-len(val))
                tile = val + blank
                print (colored(tile, colorMap[e]), end=" ")
            print ('\n')

        print ("Current point is: ", end=" ")
        print (colored(self.point, attrs=['bold']))
        print ('- - - - - - - - - - - - - - - - - - - - - - - - -')
        return

    # function isGoal
    # Check whether user achieved the goal or not

    def isGoal(self):
        if self.maxValue == 2048:
            return True
        return False

    def canMove(self):
        table = self.table
        size = self.size

        if self.freeList!= []:
            return True

        for i in range(size-1):
            for j in range(size-1):
                if table[i][j] == table[i+1][j] or table[i][j] == table[i][j+1]:
                    return True

            if table[size-1][i] == table[size-1][i+1]:
                return True
            if table[i][size-1] == table[i+1][size-1]:
                return True

        return False

    # function pickGrid
    # Pick a free grid from a table.
    # Then place [2] tile for 90% chance, [4] tile for 10% chance

    def pickGrid(self):
        size = self.size
        candidates = [2,2,2,2,2,2,2,2,2,4]

        grid = random.choice(self.freeList)
        value = random.choice(candidates)

        self.freeList.remove(grid)
        self.table[grid//size][grid%size] = value

    # function makeMove
    # This is what 2048 is about!
    # Called each and every time when the user gives an input

    def makeMove(self, usrInput):
        if usrInput == 'w':
            self.moveUp()
        elif usrInput == 's':
            self.moveDown()
        elif usrInput == 'a':
            self.moveLeft()
        elif usrInput == 'd':
            self.moveRight()
        else:
            print ('Please select a valid move')
            return 1
        return 0

    # function moveUp
    # Like other three move functions below,
    # 1) Handles the merge first and then
    # 2) Handles the blanks
    # Other move functions has similar structures, thus emit comments for them.

    def moveUp(self):
        n = self.size
        table = self.table
        freeList = self.freeList
        maxValue = self.maxValue

        for col in range(0, n):

            # Merge Handling
            for i in range(0, n-1):
                if table[i][col]!= '-':
                    for j in range(i+1, n):
                        if table[i][col] == table[j][col]:
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            table[i][col] = table[i][col] * 2
                            self.point += table[i][col]
                            maxValue = max(maxValue, table[i][col])
                            break
                        elif table[j][col] != '-':
                            break

            # Blank Handling
            for i in range(0, n-1):
                if table[i][col] == '-':
                    for j in range(i+1, n):
                        if table[j][col]!= '-':
                            table[i][col] = table[j][col]
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            freeList.remove(i*n + col)
                            break

    # function moveDown

    def moveDown(self):
        n = self.size
        table = self.table
        freeList = self.freeList
        maxValue = self.maxValue

        for col in range(0, n):
            iRange = list(range(1, n))
            iRange.reverse()

            for i in iRange:
                if table[i][col] != '-':
                    jRange = list(range(0, i))
                    jRange.reverse()
                    for j in jRange:
                        if table[i][col] == table[j][col]:
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            table[i][col] = table[i][col] * 2
                            self.point += table[i][col]
                            maxValue = max(maxValue, table[i][col])
                            break
                        elif table[j][col] != '-':
                            break

            for i in iRange:
                if table[i][col] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()
                    for j in jRange:
                        if table[j][col]!= '-':
                            table[i][col] = table[j][col]
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            freeList.remove(i*n + col)
                            break

    # function moveLeft

    def moveLeft(self):
        n = self.size
        table = self.table
        freeList = self.freeList
        maxValue = self.maxValue

        for row in range(0, n):
            for i in range(0, n-1):
                if table[row][i] != '-':

                    for j in range(i+1, n):
                        if table[row][i] == table[row][j]:
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            table[row][i] = table[row][i] * 2
                            self.point += table[row][i]
                            maxValue = max(maxValue, table[row][i])
                            break
                        elif table[row][j] != '-':
                            break

            for i in range(0, n-1):
                if table[row][i] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in range(i+1, n):
                        if table[row][j]!= '-':
                            table[row][i] = table[row][j]
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            freeList.remove(row*n + i)
                            break

    # function moveRight

    def moveRight(self):
        n = self.size
        table = self.table
        freeList = self.freeList
        maxValue = self.maxValue

        for row in range(0, n):
            iRange = list(range(1,n))
            iRange.reverse()
            for i in iRange:
                if table[row][i] != '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in jRange:
                        if table[row][i] == table[row][j]:
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            table[row][i] = table[row][i] * 2
                            self.point += table[row][i]
                            maxValue = max(maxValue, table[row][i])
                            break
                        elif table[row][j] != '-':
                            break

            for i in iRange:
                if table[row][i] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in jRange:
                        if table[row][j]!= '-':
                            table[row][i] = table[row][j]
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            freeList.remove(row*n + i)
                            break

# Main routine

table = Table()

while (table.canMove()):
    usrInput= input("Pick a move : w(up) / s(down) / a(left) / d(right) ")

    # Handles invalid inputs
    if table.makeMove(usrInput):
        continue

    # When table is full and make a move toward invalid direction, ignore it.
    try:
        table.pickGrid()
    except:
        pass

    table.printTable()

    # When the goal is achieved
    if table.isGoal():
        print ("You won !!! Your final score is: ", end =" ")
        print (table.point)
        input ("Insert any key to quit... ")

# When There's no possibly way to win
print ("You lost... Your final score is: ", end =" ")
print (table.point)
input ("Insert any key to quit... ")
