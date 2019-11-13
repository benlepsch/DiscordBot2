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
        self.firstMove = msg[3]
        self.flagsLeft = self.bombs
        self.generateGrid(self.convertMove(msg[3]))
        #self.nicePrint(self.numbersGrid)
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
            self.reset()
            return 'You lose! haha get fucked'
        
        if self.numbersGrid[move[0]][move[1]] != 0:
            self.displayGrid[move[0]][move[1]] = True
            if self.checkWinClick():
                st = self.showGrid() + '\nYou Won!'
                self.reset()
                return st
            return self.showGrid()
        
        if self.numbersGrid[move[0]][move[1]] == 0:
            # clear everything around it then do again for any zeros uncovered
            # i should probably write a function since this needs to be recursive
            self.toClear = [[move[0], move[1]]]
            for mv in self.toClear:
                self.clearZero(mv)
            return self.showGrid()

    def clearZero(self, move):
        for i in range(move[0]-1, move[0]+2):
            if i < 0:
                continue
            for j in range(move[1]-1, move[1]+2):
                if j < 0:
                    continue
                try:
                    #self.displayGrid[i][j] = True
                    #if self.numbersGrid[i][j] == 0 and not self.displayGrid[i][j]:
                    #    self.clearZero([i,j])
                    if self.numbersGrid[i][j] == 0 and not self.displayGrid[i][j]:
                        self.toClear.append([i,j])
                    
                    if not self.displayGrid[i][j]:
                        self.displayGrid[i][j] = True
                    
                except IndexError:
                    continue
    
    def flag(self, msg):
        # msg should be like "4A" or something, after conversion 4A -> [3,0]
        msg = self.convertMove(msg)
        i, j = msg
        # unflag
        if self.grid[i][j] == 'CF' or self.grid[i][j] == 'IF':
            self.grid[i][j] = 'US'
            self.flagsLeft += 1
            return self.showGrid()
        
        # not unbroken
        if self.displayGrid[i][j]:
            return 'you can\'t flag that you imbecile'
        
        if self.numbersGrid[i][j] == 'B':
            self.grid[i][j] = 'CF'
            self.flagsLeft -= 1
            if self.checkWinFlag():
                st = self.showGrid() + '\nYou Won!'
                self.reset()
                return st
            return self.showGrid()
        
        self.grid[i][j] = 'IF'
        self.flagsLeft -= 1
        return self.showGrid()

    def showGrid(self):
        out = 'Flags left: ' + str(self.flagsLeft) + '\n'
        for i in range(len(self.grid)):
            out += str(i+1) + ' '*(3-len(str(i+1))) # 2 spaces for single digit numbers, 1 for two digit numbers
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'CF' or self.grid[i][j] == 'IF':
                    out += 'F '
                    continue
                if self.displayGrid[i][j]:
                    if self.originalGrid[i][j] == 0:
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

    # two ways to win: flagging all the bombs or clicking everything except the bombs
    def checkWinFlag(self):
        if self.flagsLeft != 0:
            return False
        for i in self.grid:
            for j in i:
                if j == 'IF':
                    return False
        
        return True
    
    def checkWinClick(self):
        for i in range(len(self.displayGrid)):
            for j in range(len(self.displayGrid[0])):
                if not self.displayGrid[i][j] and self.numbersGrid[i][j] != 'B':
                    return False
        return True

    def reset(self):
        self.grid = [] 
        self.numbersGrid = [] 
        self.originalGrid = [] 
        self.displayGrid = [] 
        self.height = 0
        self.width = 0
        self.bombs = 0
        self.flagsLeft = 0
        self.running = False

ms = Minesweeper()

ms.startGame(input('Enter height, width, bombs, and first move separated by spaces: '))
ms.clear(ms.firstMove)
print(ms.showGrid())

running = True
while running:
    inpuT = input('Break/Flag + Location: ')

    if len(inpuT.split(' ')) < 2:
        print('make sure you include the location in there too')
        continue

    if inpuT.split(' ')[0].lower() == 'break':
        print(ms.clear(inpuT.split(' ')[1]))
    elif inpuT.split(' ')[0].lower() == 'flag':
        print(ms.flag(inpuT.split(' ')[1]))
    else:
        print('I didnt recognize that option, try typing break or flag')

    if not ms.running:
        running = False
        break