def display_board(board):
    for row in board:
        print (" ".join(row))
    return 
def player1Chance():
    global Count
    answer=-1
    #writing the code for player 1 input
    while(answer==-1):
        player1_choice=raw_input('Enter the position where you wanna enter the value "X"(1-9)')
        if int(player1_choice)>0 and int(player1_choice)<10:
            #need to update the display board
            if int(player1_choice)>0 and int(player1_choice)<4:
                board[0][int(player1_choice)-1]='X'
                answer=0
            if int(player1_choice)>3 and int(player1_choice)<7:
                board[1][int(player1_choice)-4]='X'
                answer=0
            if int(player1_choice)>6 and int(player1_choice)<10:
                board[2][int(player1_choice)-7]='X'   
                answer=0
    display_board(board)
    Count+=1
    return
def player2Chance():
    global Count
    answer=-1
    #writing the code for player 2 input
    while(answer==-1):
        player2_choice=raw_input('Enter the position where you wanna enter the value "O"(1-9)')
        if int(player2_choice)>0 and int(player2_choice)<10:
            #need to update the display board
            if int(player2_choice)>0 and int(player2_choice)<4:
                board[0][int(player2_choice)-1]='O'
                answer=0
            if int(player2_choice)>3 and int(player2_choice)<7:
                board[1][int(player2_choice)-4]='O'
                answer=0
            if int(player2_choice)>6 and int(player2_choice)<10:
                board[2][int(player2_choice)-7]='O'   
                answer=0
    display_board(board)
    Count+=1
    return
def whosWinning():
    if (board[0][0]=='X' and board[0][2]=='X' and board[0][1]=='X'):
        print('Player 1 Won')
        return True
    elif (board[0][0]=='O' and board[0][2]=='O' and board[0][1]=='O'):
        print('Player 2 Won') 
        return True
    elif (board[1][0]=='O' and board[1][2]=='O' and board[1][1]=='O'):
        print('Player 2 Won') 
        return True
    elif (board[1][0]=='X' and board[1][2]=='X' and board[1][1]=='X'):
        print('Player 1 Won')
        return True
    elif (board[2][0]=='X' and board[2][2]=='X' and board[2][1]=='X'):
        print('Player 1 Won')
        return True
    elif (board[2][0]=='O' and board[2][2]=='O' and board[2][1]=='O'):
        print('Player 2 Won')
        return True
    elif (board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X'):
        print('Player 1 Won')
        return True
    elif (board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O'):
        print('Player 2 Won')
        return True
    elif (board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O'):
        print('Player 2 Won') 
        return True
    elif (board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X'):
        print('Player 1 Won') 
        return True
    elif (board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X'):
        print('Player 1 Won')
        return True
    elif (board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O'):
        print('Player 2 Won') 
        return True
    elif (board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O'):
        print('Player 2 Won')
        return True
    elif (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X'):
        print('Player 1 Won')
        return True
    elif (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X'):
        print('Player 1 Won')
        return True
    elif (board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O'):
        print('Player 2 Won')    
        return True
    return False
playAgain=-1
while (playAgain==-1):
    global playAgain
    print ('Welcome to python version of Tic Tac Toe')
    board=[]
    start_point=1
    end_point=4
    for rows in xrange(3):
        global start_point
        global end_point
        board.append([])
        for columns in xrange(start_point,end_point):
            board[rows].append(str(columns))
        if end_point==4:
            start_point=4
            end_point=7
        elif end_point==7:
            start_point=7
            end_point=10
    Count=1
    display_board(board)
    while Count<10:
        player1Chance()
        won=whosWinning()
        if (won): break
        if Count<9:
            player2Chance()
            won=whosWinning()
            if (won): break
    play=raw_input('Do you wanna Play Again?(Y/N)') 
    play=play.upper()
    print (play)
    if (play=='N'):
        playAgain=0
        break                   