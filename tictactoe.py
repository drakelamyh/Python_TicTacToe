### TIC TAC TOE GAME ###
# by Drake
# first commit 12 May 2021




# for Jupyter Notebook module
# clear_output only works in Jupyter notebook and will not run in other environments
from IPython.display import clear_output

# print starting instructions
def instructionsFn():
    print("Welcome to Python Tic Tac Toe!")
    print("For this game, we will use the keyboard numpad to match numbers to the grid on a tic tac toe board.")
    print("This is how it will look like:")
    print("1 | 2 | 3 \n4 | 5 | 6 \n7 | 8 | 9\n")

instructionsFn()



# function to identify Player 1's pick (X or O)

def p1markerFn():
    
    p1_marker = 'wrong'
    
    while p1_marker not in ['X', 'O']:
        
        p1_marker = input("Player 1: Do you want to be X or O? ").upper()
        
        if p1_marker not in ['X', 'O']:            
            print("Invalid choice! (X or O only)")

    return p1_marker

p1_mark = p1markerFn()

print(p1_mark, "is selected for Player 1")




# function to assign Player 2's pick (O or X)

def p2markerFn():
        
    if p1_mark == "X":
        return "O"
    if p1_mark == "O":
        return "X"

p2_mark = p2markerFn()
print("Player 2 shall use", p2_mark, "to play.")




# function to ask if ready to play
# terminate the game if Player not ready to start

def game_starting():
    
    game_start = "wrong"
    
    while game_start not in ['YES','NO']:
        
        game_start = input("Are you ready to play? Enter Yes or No: ").upper()
        
        if game_start not in ['YES','NO']:
            print("Invalid choice! (Yes or No only)")

    if game_start == "YES":
        print("Let's Go!")
    
    if game_start == "NO":
        print("Ok let's play another time.")

    return game_start

game_start = game_starting()




# list out all conditions for tic tac toe (win / draw), else continue game

def wintest(game_list):
    if game_list[1] == game_list[2] == game_list[3] and game_list[1] != " ":
        return True
    elif game_list[4] == game_list[5] == game_list[6] and game_list[4] != " ":
        return True
    elif game_list[7] == game_list[8] == game_list[9] and game_list[7] != " ":
        return True
    elif game_list[1] == game_list[4] == game_list[7] and game_list[1] != " ":
        return True
    elif game_list[2] == game_list[5] == game_list[8] and game_list[2] != " ":
        return True
    elif game_list[3] == game_list[6] == game_list[9] and game_list[3] != " ":
        return True
    elif game_list[1] == game_list[5] == game_list[9] and game_list[1] != " ":
        return True
    elif game_list[3] == game_list[5] == game_list[7] and game_list[3] != " ":
        return True
    elif " " not in game_list:
        return "DRAW"
    else:
        return False





# function to capture Player 1's selected position

def player1_choice():
    
    p1 ='WRONG'
    within_range = False
    
    while p1.isdigit() == False or within_range == False:
    # while continue to run until digit is passed in and it is within range 
    
        p1 = input("Player 1, Choose your next position (1 - 9): ")
        
        if p1.isdigit() == False:
            print("Sorry that is not a digit!\n")
            
        if p1.isdigit():
            if int(p1) in range(1,10):  # range for 1 to 9
                within_range = True
            else:
                print("Sorry number is not within range (1-9)!\n")     
    
    return int(p1)





# function to capture Player 2's selected position

def player2_choice():
    
    p2 ='WRONG'
    within_range = False
    
    while p2.isdigit() == False or within_range == False:
    # while continue to run until digit is passed in and it is within range 
    
        p2 = input("Player 2, Choose your next position (1 - 9): ")
        
        if p2.isdigit() == False:
            print("Sorry that is not a digit!\n")
            
        if p2.isdigit():
            if int(p2) in range(1,10):  # range for 1 to 9
                within_range = True
            else:
                print("Sorry number is not within range (1-9)!\n")     
    
    return int(p2)





# function to display numbers in 3 x 3 grid
# x[0] is assigned to a random character, so that can use x[1] to x[9] in accordance to position 1 to 9 for ease of coding

def display_game(x):
    clear_output()
    print(f"{x[1]} | {x[2]} | {x[3]} \n{x[4]} | {x[5]} | {x[6]} \n{x[7]} | {x[8]} | {x[9]}\n")







# main gaming function'
# game continues until wincon = True (i.e. game win) or wincon = "DRAw" (i.e. ends in a draw)

def gaming():
    
    # First Game List
    game_list = ["!"," "," "," "," "," "," "," "," "," "]
    
    wincon = False
    
    if game_start == "NO":
        wincon = "FAIL"
    
    while wincon not in [True, "DRAW", "FAIL"]:
        
        
        game_list[player1_choice()] = p1_mark
        display_game(game_list)
        
        if wintest(game_list) == True:
            wincon = True
            print("Player 1 Wins!")
            break
        elif wintest(game_list) == "DRAW":
            wincon = "DRAW"
            print("It's a DRAW")
            break

        game_list[player2_choice()] = p2_mark
        display_game(game_list)
        
        if wintest(game_list) == True:
            wincon = True
            print("Player 2 Wins!")
            break
        elif wintest(game_list) == "DRAW":
            wincon = "DRAW"
            print("It's a DRAW")
            break
            
    if game_start != "NO":
        gameon_choice()





# function to run after each game to ask if want to play again

def gameon_choice():
    
    again = "wrong"
    
    while again not in ['YES','NO']:
        
        again = input("Do you want to play again? Enter Yes or No: ").upper()

        if again not in ['YES','NO']:
            print("Invalid choice! (Yes or No only)")

        if again == "YES":
            game_list = ["!"," "," "," "," "," "," "," "," "," "]
            gaming()

        if again == "NO":
            print("Bye bye")
            break





# function runs if game_start == "YES"
# prevent function from running if player not ready to start game

if game_start == "YES":
    gaming()




# END