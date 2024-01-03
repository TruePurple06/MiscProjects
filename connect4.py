
player1 ="Y"
player2= "R"
endGame = 0
board = list(list("o" for x in range(6)) for y in range(7))

def display():
    """"Displays board nicely"""
    for i in range(len(board)):
        print(board[i])


def posdiagonal(row,column):
    #Returns the entire diagonal in the positive direction as a string
    c = row + column
    if c < 6:
       return "".join(map(str,list(board[-x+c][x] for x in range(0,c+1))))
    else:
        return "".join(map(str,list(board[-x+c][x] for x in range(c-6,6))))

def negdiagonal(row,column):
    #Returns the entire diagonal in the negative direction as a string
    c = column - row
    if c < 0 :
       return "".join(map(str,list(board[x-c][x] for x in range(0,c+7))))
    else:
        return "".join(map(str,list(board[x-c][x] for x in range(0,6))))  
    
    
def checkWin(player,row,column):
    # checks if there is a win in the relavent rows,columns or diagonals
    global endGame
    win1 = "YYYY"
    win2 = "RRRR"
    
    fullColumn ="".join(map(str,list(board[x][column] for x in range(7))))
    fullRow = "".join(map(str,list(board[row][x] for x in range(6))))
    
    d1 = posdiagonal(row,column)
    d2 = negdiagonal(row,column)
    
    if player == player1:
        if win1 in fullColumn or win1 in fullRow or win1 in d1 or win1 in d2:
            print("Yellow wins!")
            endGame = 1
            return
    else:
        if win2 in fullColumn or win2 in fullRow or win2 in d1 or win2 in d2:
            print("Red wins!")
            endGame = -1
            return
        
    


def play(player):
    #allows input, as well as adding gravity to the peices
    column = 0
    while column > 6 or column < 1:
        column = int(input("enter the column your want to place you slot in(1-6) "))
    column = column - 1 
    for i in range(1,8):
        if board[7-i][column] == "o":
            board[7-i][column] = player
            row = 7-i
            break
    display()
    checkWin(player,row,column)
    

while endGame == 0:
    # plays the game until win condition is met
    play(player1)
    if endGame != 0:
        break
    play(player2)
    







    
    



