#Variables
square = []
square = ["_" for x in range(10)] 
#gameInSession = True
isUserTurn = True

#functions
def DrawBoard():
    #variables
    '''
    square1 = square2 = square3 = " "
    square4 = square5 = square6 = " "
    square7 = square8 = square9 = " "
    '''
    
    print(' ',square[1],'  |  ',square[2],'  |  ',square[3],' ')
    print("------|-------|------")
    print(' ',square[4],'  |  ',square[5],'  |  ' ,square[6],' ')
    print("------|-------|------")
    print(' ',square[7],'  |  ',square[8],'  |  ' ,square[9],' ')

def UpdateBoard(typeChar,pos):
    #print("UpdateBoard pointers contain: typeChar: ", typeChar, "pos: ", pos)#DEBUGGING LINE
    
    square[int(pos)] = typeChar
    DrawBoard()

def UserInput():
    chara, pos = input("Enter a value from 1-9: ").split() 
    chara = chara.upper()
    print("Charachter: ", chara)
    print("Columns number: ", pos) 
    print() 
    return chara, pos

def CheckTurn(UserTurn):
    if UserTurn == True:
        UserTurn = False
    else:
        UserTurn = True
    return UserTurn

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
    if square[1] == 'O' and square[5] == 'O' and square[9] == 'O': winner = "O"
    elif square[3] == 'O' and square[5] == 'O' and square[7] == 'O': winner = "O"
    #Stright Horizontal Win for Team X
    elif square[1] == 'O' and square[2] == 'O' and square[3] == 'O': winner = "O"
    elif square[4] == 'O' and square[5] == 'O' and square[6] == 'O': winner = "O"
    elif square[7] == 'O' and square[8] == 'O' and square[9] == 'O': winner = "O"
    #Straight Win Verticle for Tem X
    elif square[1] == 'O' and square[4] == 'O' and square[7] == 'O': winner = "O"
    elif square[2] == 'O' and square[5] == 'O' and square[8] == 'O': winner = "O"
    elif square[3] == 'O' and square[6] == 'O' and square[9] == 'O': winner = "O"
    
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

#main
#Init secetion
DrawBoard()
print(WinningSequences())
while WinningSequences() == True:
    #take user input 
    #print("Main section output ",UserInput()) #DEBUGGING LINE
    typeChar,pos = UserInput()

    #update the game
    #print("Main section output, UserInput returns : ", typeChar, " ", pos) #DEBUGGING LINE
    UpdateBoard(typeChar,pos)
    WinningSequences()
    isUserTurn = CheckTurn(isUserTurn)
    #check to see whos turn
    if WinningSequences == True and isUserTurn == False:
        print("It is computer's turn!")
