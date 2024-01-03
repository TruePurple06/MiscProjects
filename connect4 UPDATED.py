import random
player1 ="Y"
player2= "R"
wincase1 = ["oYYY","YoYY","YYoY","YYYo"]
wincase2 = ["oRRR","RoRR","RRoR","RRRo"]
board = list(list("o" for x in range(6)) for y in range(7))

def display():
    """"Displays board nicely"""
    for i in range(len(board)):
        print(board[i])


def posdiagonal(row,column):
    #Returns the entire diagonal in the positive direction as a string
    c = row + column
    if c < 6:
        return list(board[-x+c][x] for x in range(0,c+1))
    else:
        return list(board[-x+c][x] for x in range(c-6,6))

def negdiagonal(row,column):
    #Returns the entire diagonal in the negative direction as a string
    c = column - row
    if c < 0 :
        return list(board[x-c][x] for x in range(0,c+7))
    else:
        return list(board[x-c][x] for x in range(0,6))
    
    
def checkWin(player,row,column):
    # checks if there is a win in the relavent rows,columns or diagonals
    win1 = "YYYY"
    win2 = "RRRR"
    
    fullColumn =list(board[x][column] for x in range(7))
    FCstring = "".join(fullColumn)
    
    fullRow = list(board[row][x] for x in range(6))
    FRstring = "".join(fullRow)
    
    d1 = "".join(posdiagonal(row,column))
    d2 = "".join(negdiagonal(row,column))
    
    if player == player1:
        if win1 in FCstring or win1 in FRstring or win1 in d1 or win1 in d2:
            print("Yellow wins!")
            exit()
        calcRed(fullColumn,fullRow,d1,d2,row,column,FCstring,FRstring)
    else:
        if win2 in FCstring or win2 in FRstring or win2 in d1 or win2 in d2:
            print("Red wins!")
            exit()

        
    


def play(player,column = 0):
    #allows input, as well as adding gravity to the peices
    while column > 6 or column < 1:
        column = int(input("\nenter the column your want to place you slot in(1-6) "))
    column = column - 1 
    for i in range(1,8):
        if board[7-i][column] == "o":
            board[7-i][column] = player
            row = 7-i
            break
    if player == player2:
        print(f"\nRed places a piece in column {column+1}")
    display()
    checkWin(player,row,column)
    

def calcRed(fullColumn,fullRow,d1,d2,row,column,FCstring,FRstring):
    block = "YYY"
    
    if block in FCstring:
        play(player2,column+1)
    
    elif block in FRstring and row == 6:
        for i in range(0,5):
            if fullRow[i] == "o" and fullRow[i+1] == "Y":
                play(player2,i+1)
                break
            elif i>0 and fullRow[i] == "o" and fullRow[i-1] == "Y":
                play(player2,i+1)
                break
    
    
    else:
        play(player2,random.randint(1,6))
    pass

def isValid(row,column):
    if row == 6:
        return True
    elif board[row+1][column] != "o":
        return True
    else:
        return False 


def bruteColumn(wincase):
    for i in range(6):
        column = list(board[x][i] for x in range(7))
        Cstring = "".join(column)
        if wincase[-1] in Cstring:
            return i
def bruteRow(player,wincase):
    for i in range(7):
        row = list(board[6-i][x] for x in range(6))
        Rstring = "".join(row)
        for win in wincase:
            if win in Rstring:
                for j in range(6):
                    if j != 5:
                        if row[j] == "o" and row[j+1] == player and isValid(i,j) == True:
                            return j
                    elif row[j] == "o" and row[j-1] == player and isValid(i,j) == True:
                        return j

def bruteDiag(player,wincase):
    for i in range(0,7,6):
        for j in range(0,6):
            diag1 = posdiagonal(i,j)
            Dstring = "".join(diag1)
            for win in wincase:
                if win in Dstring:
                    for k in range(len(diag1)):
                        if k != len(diag)-1:
                            if diag1[k] == "o" and diag1[k+1] == player and isValid(len(diag1)-1-k,k) == True:
                                return k
                        elif row[k] == "o" and row[k-1] == player and isValid(len(diag1)-1-k,k) == True:
                            return k
                




while True:
    # plays the game until win condition is met
    play(player1)
    







    
    



