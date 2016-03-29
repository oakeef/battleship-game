__author__ = 'Evan'

#create variables to store the answer board and the game board
board = []
board2 = []

# function that prints the board
def print_board(x):
    #this prints the top part of the board
    print("  A B C D E F G H I J")
    #this for loop goes through i in the row and increases the counter by one (learned this neat enumerate trick)
    for i, row in enumerate(x, 1):
        #print the iterated number + a space + the wor in the board.
        print(str(i)+" "+" ".join(row))

#this function does a really cool thing where it find the unicode of the letter and subtract it from the unicode of A
#this allows it to figure out what column it is by number since the unicode for the letters increases by one each time
#my friend taught me this part
def get_column(x):
    return ord(x)-ord("A")

#this function splits the value we get from the user input into 2 sections and puts them in a list.
#this way we know the coordinates for the grid. It seperates the first part and second part into strings.
def missile_split(x):
    #this one seperates the first letter
    column = get_column(x[:1])
    #this part seperates the second part, the number and subtracts it by one since the coordinates start at 0,0
    row = int(x[1:]) - 1
    #this returns the 2 new values as a list
    return [column, row]

#this function checks for a hit by comparing the board coordinates with coordinates we supply.
def check_hit(x):
    board_value = board[x[1]][x[0]]
    return board_value == "1"

#this function checks to see if you have a valid input
def vaild_input(x):
    #makes sure the length of the input is at least 2 otherwise it is invalid
    if len(x) < 2:
        return False
    #this splits the input like the other function
    column = x[:1]
    row = int(x[1:])
    #returns true only if the first input is a letter from A-J and the second is a number less than or equal to 10
    return column in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] and row <= 10

#this opens the map file in read mode and puts it in variable map
with open('map.txt', 'r') as map:
    #this loop goes through every line in map and appends it to the board list, removes the ","
    for line in map:
        board.append(line.rstrip().split(','))

#this creates the second board. the one the player will see.
for x in range(10):
    board2.append(["_"] * 10)

print("Let's play Battleship!")

#run the function to print the game board
print_board(board2)

#create 2 variables for turn count and hit count.
turn_count = 0
hit_count = 0

#while loop goes until turns are more than 30
while turn_count < 30:
    #input for misle coordinates in upper case
    missile_input = input("Choose your target (EX: A1): ").upper()
    #check for valid input
    if vaild_input(missile_input):
        #if input is valid run split function to find coordinates and put them in list
        missile = missile_split(missile_input)
        #run check hit function to see if missile hits target
        if check_hit(missile):
            #if that is ture than hit count goes up by one and board 2 coordinate changes to X
            hit_count += 1
            board2[missile[1]][missile[0]] = "X"
            print("Hit!")
        else:
            #if it is not a hit than board 2 coordinates are changed to O
            board2[missile[1]][missile[0]] = "O"
            print("Miss!")
        #turn count goes up by one each turn whether it is hit or miss but only if it is a valid move
        turn_count += 1
        print_board(board2)
        #if the hit count gets to 17 than the game is over and you win
        if hit_count == 17:
            print("You Win!")
            break
    #if the move is not valid you try again
    else:
        print("Invalid Input, try again.")
        print_board(board2)