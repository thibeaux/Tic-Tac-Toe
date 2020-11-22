import random
#Global Variables
square = []
square = [" " for x in range(10)] 
pos = 0
isUserTurn = True
positions = [1,2,3,4,5,6,7,8,9] #this is gloal because we need the list to be updated throughout the game, and not reset everytime PCTurn is called

#functions
def DrawBoard():
    #Draws the game bard on the terminal
    print(' ',square[7],'  |  ',square[8],'  |  ',square[9],' ')
    print("------|-------|------")
    print(' ',square[4],'  |  ',square[5],'  |  ' ,square[6],' ')
    print("------|-------|------")
    print(' ',square[1],'  |  ',square[2],'  |  ' ,square[3],' ')

def UpdateBoard(typeChar,pos):
    #Updates the game board with new moves

    #print("UpdateBoard pointers contain: typeChar: ", typeChar, "pos: ", pos)#DEBUGGING LINE
    square[int(pos)] = typeChar
    DrawBoard()

def UserInput():
    #Takes the users input and only accepts input between 1 and 9 and it has to be an integer
    pos=0
    while True:
        try:
            while not int(pos) in range(1,10):
                pos = int(input("Enter a position value 1-9: "))      
        except ValueError:
            print("Not an integer between 1-9. Try again.")
            continue
        else:
            return pos
            break 
    #chara = chara.upper()
    
    #print("Charachter: ", chara)
    #print("Columns number: ", pos) 
    #print() 
    return pos

def CheckTurn(UserTurn):
    #Will toggle between whos turn it is each time this is called. The main difference between this function and
    #XOTOGGLE is that ChekTurn deals with the boolean values and not the actual team characters 'X' and 'O' them selves.
    #Do not call this unless you mean to switch the teams. There are other ways to0 find out what team's turn it is without calling this.
    if UserTurn == True:
        UserTurn = False
    else:
        UserTurn = True
    return UserTurn
    
def XOToggle():
    #Everytime this is called the game switches teams  and returns which teams turn it is. Do not call this unless
    # you mean to switch the teams. There are other ways to0 find out what team's turn it is without calling this.
    #Same thing with CheckTurn.
    if isUserTurn == True:
        return "X"
    else:
        return "O"

def isBoardFull():
    #Checks if board is full
    #print("Square Count: " ,square.count(" "))#DEBUGGING LINE
    if square.count(" ") <= 1:
        return True
    return False
def IsBoardEmpoty():
    #Checks if board is empty
    if square.count(" ")>= 9:
        return True
    return False
    
def WinningSequences():
    winner = ""
    gameInSession = True
    #diagonal wins for team X 
    if square[1] == 'X' and square[5] == 'X' and square[9] == 'X': winner = "X"
    elif square[3] == 'X' and square[5] == 'X' and square[7] == 'X': winner = "X"
    #Stright Horizontal Win for Team X
    elif square[1] == 'X' and square[2] == 'X' and square[3] == 'X': winner = "X"
    elif square[4] == 'X' and square[5] == 'X' and square[6] == 'X': winner = "X"
    elif square[7] == 'X' and square[8] == 'X' and square[9] == 'X': winner = "X"
    #Straight Win Verticle for Tem X
    elif square[1] == 'X' and square[4] == 'X' and square[7] == 'X': winner = "X"
    elif square[2] == 'X' and square[5] == 'X' and square[8] == 'X': winner = "X"
    elif square[3] == 'X' and square[6] == 'X' and square[9] == 'X': winner = "X"
    #Team O Victory
    elif square[1] == 'O' and square[5] == 'O' and square[9] == 'O': winner = "O"
    elif square[3] == 'O' and square[5] == 'O' and square[7] == 'O': winner = "O"
    #Stright Horizontal Win for Team X
    elif square[1] == 'O' and square[2] == 'O' and square[3] == 'O': winner = "O"
    elif square[4] == 'O' and square[5] == 'O' and square[6] == 'O': winner = "O"
    elif square[7] == 'O' and square[8] == 'O' and square[9] == 'O': winner = "O"
    #Straight Win Verticle for Tem X
    elif square[1] == 'O' and square[4] == 'O' and square[7] == 'O': winner = "O"
    elif square[2] == 'O' and square[5] == 'O' and square[8] == 'O': winner = "O"
    elif square[3] == 'O' and square[6] == 'O' and square[9] == 'O': winner = "O"
    #Draw game
    elif isBoardFull() == True:
        print("Draw! Game over")
        gameInSession = False
        return gameInSession
    
    if winner == "O":
        print(" O Wins!!")
        gameInSession = False
        return gameInSession
    elif winner == "X":
        print("X Wins!!")
        gameInSession = False
        return gameInSession
    else:
        gameInSession = True
        return gameInSession
        
def SqaureIsTaken (chk):
    #checks if the square is taken by either team characters
    location = pos 
    newPos = 0 
     
    if chk == True:
        while square[location] == "X" or square[location] == "O":
            print ("This square was already taken. Please choose a different square.") 
            newPos = UserInput () 
            if square[newPos] == " ":
                chk = False 
                break
    return newPos

def ChooseRandomSquare():
    #Updates the Pc with a new random square becuase no other possible choices where available for a vicotry or defense
    newMove = random.choice(positions)
    positions.remove(newMove)
    # UpdateBoard('O',newMove)#DEBUGGING

    return newMove
def PCTurn(playerPos):
    positions.remove(playerPos) #takes the players last move and removes it from the list of possible positions
    '''=================================Offensive moves================================================='''
    '''====================== Seek Bottom Row Victory==========================='''
    if (square[1] == 'O' and square[2] == 'O') or (square[9] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[5]=='O'):
        if 3 in positions:
            newMove = 3
            positions.remove(newMove)#every instance in offensive and  deffensive moves we have to update the list by
            # removing the computers choice
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[1] == 'O' and square[3]=='O') or (square[8] == 'O' and square[5] == 'O'):
        if 2 in positions:
            newMove = 2
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[2] == 'O' and square[3] == 'O') or (square[4] == 'O' and square[7] == 'O') or (square[5] == 'O' and square[9] == 'O'):
        if 1 in positions:
            newMove = 1
            positions.remove(newMove)
            return  newMove
        else:
            return ChooseRandomSquare()
        '''===================== Seek Mid Row Victories==================================='''
    elif (square[7] == 'O' and square[1] == 'O') or (square[5] == 'O' and square[6]) == 'O':
        if 4 in positions:
            newMove = 4
            positions.remove(newMove)
            return  newMove
        else:
            return ChooseRandomSquare()
    elif ((square[4] == 'O' and square[6] == 'O') or (square[8] == 'O' and square[2] == 'O') or
        (square[9] == 'O' and square[1] == 'O') or (square[7] == 'O' and square[3] == 'O')):
        if 5 in positions:
            newMove = 5
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[3] == 'O' and square[9] == 'O') or (square[4] == 'O' and square[5] == 'O'):
        if 6 in positions:
            newMove = 6
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
        '''===========================Seek Top row Victories==================================='''
    elif (square[1] == 'O' and square[4] == 'O') or (square[8] == 'O' and square[9] == 'O') or (
            square[5] == 'O' and square[3] == 'O'):
        if 7 in positions:
            newMove = 7
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[2] == 'O' and square[5] == 'O') or (square[7] == 'O' and square[9] == 'O'):
        if 8 in positions:
            newMove = 8
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[3] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[8] == 'O') or (
            square[5] == 'O' and square[1] == 'O'):
        if 9 in positions:
            newMove = 9
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()




        '''=======================================Defensive Moves ==================================='''
        '''====================== Seek Bottom Row defense==========================='''
    elif (square[1] == 'O' and square[2] == 'X') or (square[9] == 'X' and square[6] == 'X') or (
            square[7] == 'X' and square[5] == 'X'):
        if 3 in positions:
            newMove = 3
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[1] == 'X' and square[3] == 'X') or (square[8] == 'X' and square[5] == 'X'):
        if 2 in positions:
            newMove = 2
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[2] == 'X' and square[3] == 'X') or (square[4] == 'X' and square[7] == 'X') or (
            square[5] == 'X' and square[9] == 'X'):
        if 1 in positions:
            newMove = 1
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
        '''===================== Seek Mid Row Defense ==================================='''
    elif (square[7] == 'X' and square[1] == 'X') or (square[5] == 'X' and square[6]) == 'X':
        if 4 in positions:
            newMove = 4
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif ((square[4] == 'X' and square[6] == 'X') or (square[8] == 'X' and square[2] == 'X') or
          (square[9] == 'X' and square[1] == 'X') or (square[7] == 'X' and square[3] == 'X')):
        if 5 in positions:
            newMove = 5
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[3] == 'X' and square[9] == 'X') or (square[4] == 'X' and square[5] == 'X'):
        if 6 in positions:
            newMove = 6
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
        '''===========================Seek Top row Defense ==================================='''
    elif (square[1] == 'X' and square[4] == 'X') or (square[8] == 'X' and square[9] == 'X') or (
            square[5] == 'X' and square[3] == 'X'):
        if 7 in positions:
            newMove = 7
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[2] == 'X' and square[5] == 'X') or (square[7] == 'X' and square[9] == 'X'):
        if 8 in positions:
            newMove = 8
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
    elif (square[3] == 'X' and square[6] == 'X') or (square[7] == 'X' and square[8] == 'X') or (
            square[5] == 'X' and square[1] == 'X'):
        if 9 in positions:
            newMove = 9
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare()
        '''===========================default move============================================'''
    else:
        return ChooseRandomSquare()


#main
'''Init section'''
DrawBoard()
pos = 0
userPos = 0
#print(WinningSequences())
while WinningSequences() == True:
    if isUserTurn == True:
        #take user input
        #print("Main section output ",UserInput()) #DEBUGGING LINE
        userPos = UserInput()
        pos = userPos
        #update the game
        #print("Main section output, UserInput returns : ", typeChar, " ", pos) #DEBUGGING LINE
        if square[pos] == "X" or square[pos] == "O":
            pos = SqaureIsTaken(True)

    if isUserTurn == False:
        PCpos = PCTurn(pos)
        pos = PCpos
    #print(pos)#DEBUGLine
    UpdateBoard(XOToggle(),pos)
    WinningSequences()
    isUserTurn = CheckTurn(isUserTurn)
    print(XOToggle(), "'s turn...")
    #print(positions) #DEBBUGGINGLINE

