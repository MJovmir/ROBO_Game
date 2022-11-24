# 1d Robo Game -> loop
from os import system
from tabnanny import check

# x ----R----->
# controls: "a" - left, "d" - right

Length = 30
roboX  = 5
bomb1 = 10
bomb2 = 20 
heart = 30
option = ""
roboHP = 100
roboBT = 100
bombExploded = False
###### Game loop #######
while True:
####################### DRAW MAP #########################
    system("cls")
    
    print('\n')

    for x in range(1, Length + 1):    # 1...10
        if x == roboX and (x == bomb1 or x == bomb2):
            print("💧", end=" ")
            bombExploded = True 
        
        elif x == roboX and x == heart:
                print("⛇", end=" ") 
        elif x == roboX:
            print("⛄", end=" ")
        elif x == bomb1:
            print("💣", end=" ")
            # if bombExploded == True:
            #     print("_", end="")
                
        elif x == bomb2:
            print("💣", end=" ") 
            #if bombExploded == True:
                #     print("_", end="")
        elif x == heart:
            print("💜", end=" ") 
            
        else:
            print(".", end=" ")
    print('\n')        
    print("HP:", roboHP, "%")
    if roboHP == 101 or roboHP >= 101:
        print("HP FULL")
    print("Battery:", roboBT, "%")
    if roboBT == 101 or roboBT >= 101:
        print("POWER OVERLOAD")
    print('\n')
####################### DRAW MAP #########################
####################### READ INPUT #########################
    option = input(">>> ")
####################### READ INPUT #########################
####################### DECIDE #########################
    if option == "a" and roboX > 1:  # move left
        roboX -= 1
        roboBT -= 1     # robo Battery 
    if option == "d" and roboX < 30:  # move right
        roboX += 1
        roboBT -= 1     # robo Battery 
    # check if bomb
    if roboX == bomb1 or roboX == bomb2:
        roboHP -= 10  
        roboBT >= 0
        
        
    # check if HEART    
    if roboX == heart:
        roboHP += 20        
        roboBT += 5
    
    if option == "x" or roboHP == 0 or roboBT == 0:  # exit
        system("cls")
        print("Thank you for playing!!! ")
        break
         
####################### DECIDE #########################
