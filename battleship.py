import os
import time
import sys
from random import randint

"""
MISSING stuffs /TODO:


def angle(rng): 
    if rng == true:
        gen random angle
    usr_angle = input("vertical ")  

Description:::: 
0 = water
1 = guess
2 = already guessed
3 = ship
4 = shipdamaged
5 = ship sunked

"""

def headline():
    print('\033[95m'+ """                                                         
                    ._         ___   .___________.___________. __       _______     _______. __    __   __  .______   
                |   _  \      /   \  |           |           ||  |     |   ____|   /       ||  |  |  | |  | |   _  \  
                |  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__     |   (----`|  |__|  | |  | |  |_)  | 
                |   _  <    /  /_\  \    |  |        |  |     |  |     |   __|     \   \    |   __   | |  | |   ___/  
                |  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____.----)   |   |  |  |  | |  | |  |      
                |______/  /__/     \__\  |__|        |__|     |_______||_______|_______/    |__|  |__| |__| | _|      
                                                                                                                    \n"""+'\x1b[0m')


def make_grid(size): # create x*x grid
    return [[0] * size for _ in range(size)]

def grid_final(grids): # col naming
    grids[0][0] = " "
    alphabet = "ABCDEFGHIJKLMNOP"
    x=1
    while x < len(grids[0]):
        grids[0][x] = x
        grids[x][0] = alphabet[((x)-1)]
        x += 1

    return grids


def print_grid(grid): # printing the grids properly
    #os.system("clear")
    for row in grid:
        print(row)

def alphabet(x): #alphabet
    return {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10        
    }[x]

def usr_coords():
    
    try:        
        row = input("Letter :" )
    except KeyError:
        row = input("Now try with letters :" )

    try:
        col = int(input("number :" ))
    except ValueError:
        col = int(input("Now try with numbers :" ))

    row = alphabet(row)

    if row == 0 and col is row:
        print("invalid input")      
    

    coords = [row,col]     
    return  coords

def placeBoat(grids):
    ships = {
    "destroyer": [("size",2),("db",4)],
    "cruiser" :  [("size", 3), ("db", 2)],
    "submarine" :  [("size", 3), ("db", 1)],
    "battleship" :  [("size", 4), ("db", 2)],
    "carrier" :  [("size", 5), ("db", 1)],    
}
    shipsOnBoard = []
    print("place your ships")

    for ship in ships:
        x = ships[ship][1][1]
        while x != 0:            
            print("place: "+str(ship)+" | Size: "+str(ships[ship][0][1])+" | "+str(x)+" ship left to place" )
            shipsOnBoard = (usr_coords())
            grids[shipsOnBoard[0]][shipsOnBoard[1]] = 3
            print_grid(grids)
            x -= 1


    """
    for ship in ships:
        for
        shipsOnBoard.append(usr_coords())
        shipsOnBoard.append(ships[ship][0][1])
        shipsOnBoard.append(ships[ship][1][1])
    """


    return shipsOnBoard



def menu():
    os.system('clear')
    headline()
    '''
    choice = input('\033[94m'+"""                      
                            A:    One vs One                      
                            B:    One vs CPU                     
                            C:    Credit                       
                            Q:    EXIT                      
                            Please enter your choice: """+'\x1b[0m')
    '''
    choice = "b"
    if choice == "A" or choice =="a":
        one_vs_one()
    elif choice == "B" or choice =="b":
        main()
    elif choice == "C" or choice =="c":
        credit()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B or C")
        time.sleep(3)
        menu()

def one_vs_one():
   pass
    
def one_vs_cpu():
   pass

def credit():
    pass
    

def coordCheck(guess, grid):
    x =guess[0]
    y =guess[1]
    if grid[x][y] == 0:
        print("missed")
    elif grid[x][y] == 1:
        print("already tried")
    elif grid[x][y] == 2:
        print("ship found")
    elif grid[x][y] == 3:
        print("shipdamaged")
    elif grid[x][y] == 4:
        print("already tried")      
    

def main(): #
    grids = make_grid(11)
    grids = grid_final(grids)
    print_grid(grids)
    f = "k"#input("Enter your name commander: " )
    playerShips = placeBoat(grids)
    #grids[playerShips[0][0]][playerShips[0][1]] = 3        
    while True:        
        print("\n")
        print_grid(grids)        
        print("Commander " +f + " turn")
        coords = usr_coords()
        coordCheck(coords, grids)
        grids[coords[0]][coords[1]] += 1
        pass

        

if __name__ == "__main__":
    menu()