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
bomb1Exploded = False
bomb2Exploded = False

###### Game loop #######
while True:
####################### DRAW MAP #########################
    system("cls")
    
    print('\n')

    for x in range(1, Length + 1):    # 1...10
        if x == roboX and x == bomb1:
            print("💧", end=" ")
            x = bomb1 = bomb1Exploded
            bomb1Exploded = True
            
        elif x == roboX and x == bomb2:
            print("💧", end=" ")
            x = bomb2 = bomb2Exploded
            bomb2Exploded = True
            
        elif x == roboX and x == heart:
            print("⛇", end=" ") 
            
        elif x == roboX:
            print("⛄", end=" ")
        
        elif x == bomb1 and bomb1Exploded == False:
            print("💣", end=" ")    
                
        elif x == bomb2 and bomb2Exploded == False:
            print("💣", end=" ") 
            
        elif x == heart:
            print("💜", end=" ") 
            
        else:
            print(".", end=" ")
    print('\n')        
    print("HP:", roboHP, "%")
    print("Battery:", roboBT, "%")
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
        
    # check if HEART    
    if roboX == heart:
        roboHP += 20
        roboBT += 5
    
    if option == "x" or roboHP == 0 or roboBT == 0:  # exit
        system("cls")
        print("Thank you for playing!!! ")
        break
    if option == "x" or roboHP > 100 or roboBT > 100:
        system("cls")
        print("YOU WIN!")
        break  
####################### DECIDE #########################
