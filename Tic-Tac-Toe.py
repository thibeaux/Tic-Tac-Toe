#Variables
square = []
square = [" " for x in range(10)] 
pos = 0
isUserTurn = True

#functions
def DrawBoard():
    #Formats the game board
    print(' ',square[7],'  |  ',square[8],'  |  ',square[9],' ')
    print("------|-------|------")
    print(' ',square[4],'  |  ',square[5],'  |  ' ,square[6],' ')
    print("------|-------|------")
    print(' ',square[1],'  |  ',square[2],'  |  ' ,square[3],' ')

def UpdateBoard(typeChar,pos):
    #Updates the board with two inputs, a character type (X or O) and a position
    square[int(pos)] = typeChar
    DrawBoard()

def UserInput():
    #Takes user input.
    #This function checks to see if user has inputed a valid argument. It only accepts integers between 1 and 9. And also protects against character inputs with try/except. If a user inputs wrong data, then the program will loop this function until valid input is entered.
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

    return pos

def CheckTurn(UserTurn):
	#Determines whos turn it is
    if UserTurn == True:
        UserTurn = False
    else:
        UserTurn = True
    return UserTurn
    
def XOToggle():
    #Toggles between X and O based on whether it is Users(X) turn or not
    if isUserTurn == True:
        return "X"
    else:
        return "O"

def isBoardFull():
    #This function is for checking if the board is full of X's and O's by counting how many squares have the space character
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
    #Declare winner
    if winner == "O":
        print(" O Wins!!")
        gameInSession = False
        return gameInSession
    elif winner == "X":
        print("X Wins!!")
        gameInSession = False
        return gameInSession
    #No Winner Detected
    else:
        gameInSession = True
        return gameInSession
        
def SqaureIsTaken (chk):
	#Checks if square is taken. For example, if a user types in the number 5 and there is already a character there, the program will loop this function until player enters a new position that is valid or has a space character in it not a X or O.
    location = pos 
    newPos = 0 
     
    if chk == True:
        while square[location] == "X" or square[location] == "O": #tests sqaure containing X or O 
            print ("This square was already taken. Please choose a different square.") 
            newPos = UserInput () #promtps user for another square selection
            if square[newPos] == " ":#test if input was valid, If true then breaks the loop
                chk = False 
                break
    return newPos

#main
#Initialization
DrawBoard()

#Game is in motion
while WinningSequences() == True:
    #take user input 
    pos = UserInput()
    
    #update the game
    #IF statement tests to see if the input is a valid input by testing the contents of a square. If a square already has an X or O, then go to SquareIsTaken and store the return value into pos.
    if square[pos] == "X" or square[pos] == "O":
       pos = SqaureIsTaken(True)
    UpdateBoard(XOToggle(),pos)
    WinningSequences() #tests for winning sequences on board
    isUserTurn = CheckTurn(isUserTurn)#checks whos turn it is
    print(XOToggle(), "'s turn...")
