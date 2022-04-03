from random import randint  
a=randint(1,2)

def choose_first():
    return a
       
from IPython.display import clear_output

def display_board(board):
    print('    |   |   ')
    print(f'  {board[7]} | {board[8]} | {board[9]}')
    print('    |   |   ')
    print('-------------')
    print('    |   |   ')
    print(f'  {board[4]} | {board[5]} | {board[6]}')
    print('    |   |   ')
    print('-------------')
    print('    |   |   ')
    print(f'  {board[1]} | {board[2]} | {board[3]}')
    print('    |   |   \n')    

def place_marker(board, marker, position):
    board[position] = marker.upper()    

def full_board_check(board):
    for x in range(1,10):
        if (board[x]==' '):
            return False
    return True    

def win_check(board, mark):
    return((board[7]==board[8]==board[9]== mark) or
           (board[4]==board[5]==board[6]== mark) or
           (board[1]==board[2]==board[3]== mark) or
           (board[7]==board[4]==board[1]== mark) or 
           (board[8]==board[5]==board[2]== mark) or
           (board[9]==board[6]==board[3]== mark) or
           (board[7]==board[5]==board[3]== mark) or
           (board[1]==board[5]==board[9]== mark)  )

def replay():
    r=input('Do You Want To Play Again??? Yes or No :  \n ')
    return (r.upper()[0]=='Y')

def space_check(board, position):
    return board[position] ==' '

def Result():
    if win_check(ib,P[1].upper()):
            print('Congralutions Player1 has Won!!! \n')
            return True
            
    if win_check(ib,P[2].upper()):
            print('Congralutions Player2 has Won!!!\n')
            return True
    
    if full_board_check(ib):
            print('Game has been Drawen :( \n')
            return True
                
def Ready ():
    global a
    i=0
    p=0 
    
    print(f'Player{a} will take first turn\n')
    p1=input(f'Player{a} Ready??? \n')
    
    if p1.upper()[0]!='Y':           
        while i<=2:
            p1=input(f'Player{a} ready now???\n')
            if p1.upper()[0]=='Y':
                break
            if a==1:
                a += 1
            else:
                a -= 1
            i +=1
                  
    if p1.upper()[0]=='Y':
        if p!=0:
            print('lets play again!!!\n')
        else:
            print('lets play!!! \n')
    else:
        print("Since none of the Player's are ready to play ")
        print('The Game Is Abandoned :( ')
        print('OK Bye!! :( ') 
        return True

def pos_check(pos):
    if (0<pos<10):
        if space_check(ib,pos)==False :
            print('ERROR!!!!')
            print('Position Is Occupied\n')
    else:    
        print('ERROR!!!!')    
        print('position is out off limit(Numbers b/w 1 to 9 only allowed)\n') 
        
    if (0<pos<10) and not(space_check(ib,pos)==False):
        return True
    
def player_input():
    while True:
        player_inp=input(f'Player{a} X or O????').upper()
        if (player_inp=='X' or player_inp=='O'):
            if player_inp == 'X':
                return ['X','O']
            else:
                return ['O','X']
            break
        else:
            print('ERROR!!!!!')
            print('Invalid input,only X and O allowed')
            
def player_move():
    global a
    while True:
        t='first'
        try:
            pos=int(input(f"Player{a} what's your {t} move??? \n"))
        except:
            print('ERORR!!!')
            print('Please enter a number\n')
        else:
            if pos_check(pos):
                break 
    place_marker(ib,P[a],pos)
    display_board(ib)
    
    if a==1:
        while True:
            try:
                pos=int(input(f"Player2 what's your {t} move??? \n"))
            except:
                print('ERORR!!!')
                print('Please enter a number\n')
            else:
                if pos_check(pos):
                    break
        place_marker(ib,P[2],pos)
        display_board(ib)
    else:
        while True:
            try:
                pos=int(input(f"Player1 what's your {t} move??? \n"))
            except:
                print('ERORR!!!')
                print('Please enter a number\n')
            else:
                if pos_check(pos):
                    break
        place_marker(ib,P[1],pos)
        display_board(ib)
                
    while True:
        t='next'
        while True:
            pos=int(input(f"Player{a} what's your {t} move??? \n"))
            if pos_check(pos):
                break
        place_marker(ib,P[a],pos)
        display_board(ib) 
                
        if Result():
            p=1  
            break
                
        if a==1:
            a += 1
        else:
            a -= 1 


print('Welcome to Tic Tac Toe! \n')

while True:
#To decide whch player makes the first move    
    turn=choose_first()

    R=Ready()
    if R:
        break
    
#initial board
    ib=[' ']*10
    display_board(ib)  
        
    if turn==1:
        P=[0] + player_input()
    else:
        P=[0] + player_input()[::-1]
       
    player_move()
                           
    if not replay():
        print('OK Bye!!')
        break
        