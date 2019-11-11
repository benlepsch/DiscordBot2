import discord, asyncio
from random import randint

#from token_folder import token

class Minesweeper():
    def __init__(self):
        self.grid = [] # correct flags, incorrect flags, empty space, and unbroken space (as 'CF', 'IF', 'ES', and 'US')
        self.numbersGrid = [] # holds the numbers that will be displayed
        self.originalGrid = [] # just bomb or no bomb
        self.displayGrid = [] # True or False
        self.height = 0
        self.width = 0
        self.bombs = 0
        self.running = False
    
    def incSurrounding(self, arr, y, x):
        # increments the surrounding values of arr[y][x]
        for i in range(y-1, y+2):
            if i < 0:
                continue
            for j in range(x-1, x+2):
                if j < 0:
                    continue
                try:
                    if arr[i][j] != 'B':
                        arr[i][j] += 1
                except IndexError:
                    continue
    
    def convertMove(self, move):
        # move is 4C, needs to turn into [4,3]
        row = int(''.join(list(move)[:len(move)-1])) - 1 # need to slice so i can get multiple digit numbers
        col = list(move)[len(move)-1] # but this is just a single char

        if ord(col.lower()) > ord('z') or ord(col.lower()) < ord('a'):
            return 'time to break'
        
        col = ord(col.lower()) - 97 # convert to letter (or other unicode character)
        return [row, col]

    def generateGrid(self, fm):
        # initialize the arrays to default values
        for i in range(self.height):
            self.grid.append([])
            self.numbersGrid.append([])
            self.originalGrid.append([])
            self.displayGrid.append([])
            for j in range(self.width):
                self.grid[i].append('US')
                self.numbersGrid[i].append(0)
                self.originalGrid[i].append(0)
                self.displayGrid[i].append(False)
        #print(self.height)
        #print(self.width)
        #print(self.originalGrid)
        while self.bombs > 0:
            y = randint(0, self.height-1)
            x = randint(0, self.width-1)

            dy = abs(y - fm[0])
            dx = abs(x - fm[1])

            if dy < 2 and dx < 2:
                continue
            
            self.bombs -= 1
            self.numbersGrid[y][x] = 'B'
            #print(y)
            #print(x)
            self.originalGrid[y][x] = 1
            self.incSurrounding(self.numbersGrid, y, x)



    def startGame(self, msg):
        # msg looks like "10 30 20 4C"
        # should be height width bombs first_move
        if self.running:
            return 'There\'s already a game running'
        
        msg = msg.split()
        if int(msg[2]) > 26:
            return 'Can\'t have a width bigger than 26'
        
        self.running = True
        self.height = int(msg[0])
        self.width = int(msg[1])
        self.bombs = int(msg[2])

        self.generateGrid(self.convertMove(msg[3]))
        self.nicePrint(self.numbersGrid)
        #return(self.showGrid())
        # TODO: handle first move here since its different than the rest

    def clear(self, msg):
        # msg should be like "4A" or something, after conversion 4A -> [3,0]
        move = self.convertMove(msg)

        if self.grid[move[0]][move[1]] == 'CF' or self.grid[move[0]][move[1]] == 'IF': # can't click a flag
            return 'You can\'t click a flag'
        
        if self.displayGrid[move[0]][move[1]]: # it's already revealed
            return 'That space is already clicked'
        
        if self.numbersGrid[move[0]][move[1]] == 'B':
            self.grid = [] 
            self.numbersGrid = [] 
            self.originalGrid = [] 
            self.displayGrid = [] 
            self.height = 0
            self.width = 0
            self.bombs = 0
            self.running = False
            return 'You lose! haha get fucked'
        
        if self.numbersGrid[move[0]][move[1]] != 0:
            self.displayGrid[move[0]][move[1]] = True
        
        if self.numbersGrid[move[0]][move[1]] == 0:
            # clear everything around it then do again for any zeros uncovered
            # i should probably write a function since this needs to be recursive
            self.clearZero(move)

    def clearZero(self, move):
        for i in range(move[0]-1, move[0]+2):
            if i < 0:
                continue
            for j in range(move[1]-1, move[1]+2):
                if j < 0:
                    continue
                try:
                    self.displayGrid[i][j] = True
                    if self.numbersGrid[i][j] == 0 and not self.displayGrid[i][j]:
                        self.clearZero([i,j])
                except IndexError:
                    continue
    
    def flag(self, msg):
        # msg should be like "4A" or something, after conversion 4A -> [3,0]
        msg = self.convertMove(msg)

    def showGrid(self):
        out = ''
        for i in range(len(self.grid)):
            out += str(i+1) + ' '*(3-len(str(i+1))) # 2 spaces for single digit numbers, 1 for two digit numbers
            for j in range(len(self.grid[0])):
                if self.displayGrid[i][j]:
                    if self.grid[i][j] == 'CF' or self.grid[i][j] == 'IF':
                        out += 'F '
                    elif self.originalGrid[i][j] == 0:
                        out += (str(self.numbersGrid[i][j]) + ' ' if self.numbersGrid[i][j] != 0 else '- ')
                    elif self.grid[i][j] == 'US':
                        out += 'O '
                else:
                    out += 'O '
            out += '\n'
        
        out += '   '
        for i in range(len(self.grid[0])):
            out += chr(i + 65) + ' '
        
        return out
    
    def nicePrint(self, arr):
        out = ''
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                out += str(arr[i][j]) + ' '
            out += '\n'
        print(out)

ms = Minesweeper()
ms.startGame('10 10 15 5D')
print(ms.showGrid() + '\n')
ms.clear('5D')
print(ms.showGrid())
#print(ms.nicePrint(ms.displayGrid))