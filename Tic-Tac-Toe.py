#Variables
square = []
square = [" " for x in range(10)] 
pos = 0
isUserTurn = True

#functions
def DrawBoard():
    #variables
    print(' ',square[7],'  |  ',square[8],'  |  ',square[9],' ')
    print("------|-------|------")
    print(' ',square[4],'  |  ',square[5],'  |  ' ,square[6],' ')
    print("------|-------|------")
    print(' ',square[1],'  |  ',square[2],'  |  ' ,square[3],' ')

def UpdateBoard(typeChar,pos):
    #print("UpdateBoard pointers contain: typeChar: ", typeChar, "pos: ", pos)#DEBUGGING LINE
    square[int(pos)] = typeChar
    DrawBoard()

def UserInput():
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
    if UserTurn == True:
        UserTurn = False
    else:
        UserTurn = True
    return UserTurn
    
def XOToggle():
    if isUserTurn == True:
        return "X"
    else:
        return "O"

def isBoardFull():
    #print("Square Count: " ,square.count(" "))#DEBUGGING LINE
    if square.count(" ") <= 1:
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

#main
#Init secetion
DrawBoard()
#print(WinningSequences())
while WinningSequences() == True:
    #take user input 
    #print("Main section output ",UserInput()) #DEBUGGING LINE
    pos = UserInput()
    #update the game
    #print("Main section output, UserInput returns : ", typeChar, " ", pos) #DEBUGGING LINE
    
    if square[pos] == "X" or square[pos] == "O":
       pos = SqaureIsTaken(True)
    
    UpdateBoard(XOToggle(),pos)
    WinningSequences()
    isUserTurn = CheckTurn(isUserTurn)
    print(XOToggle(), "'s turn...")
