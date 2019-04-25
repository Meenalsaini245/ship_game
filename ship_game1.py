print()
import numpy as np                                     
import copy
matrix= np.array([['01','02','03','04','05','06','07','08','09','10'],                     
         ['11','12','13','14','15','16','17','18','19','20'],
         ['21','22','23','24','25','26','27','28','29','30'],
         ['31','32','33','34','35','36','37','38','39','40'],                 
         ['41','42','43','44','45','46','47','48','49','50'],
         ['51','52','53','54','55','56','57','58','59','60'],
         ['61','62','63','64','65','66','67','68','69','70'],
         ['71','72','73','74','75','76','77','78','79','80'],
         ['81','82','83','84','85','86','87','88','89','90'],
        ['91','92','93','94','95','96','97','98','99','100']])
        
exempt_list1=['09','10','19','20','29','30','39','40','49','50','59','60','69','70','79','80','89','90','99','100']             # exempt_list1 for horizontal position
exempt_list2=['81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']             # exempt_list2 for vertical position

print(matrix)                                                                               
print()
player1_list=[]                                                                                  
player2_list=[]                                                              
def set_ship_location(player,direction,board):                                                                                  # function for the ship location 
    global player1_list
    global player2_list   
                                                                                     
    ship_location=input(f'{player}, Enter your Ship location: ')                                                                # ship location entered                                                      
    if direction=='v':                                                                                                          # v is for vertical location                                                
        while ship_location in exempt_list2:                                                                                    # if the location entered is in the exempt list2                                         
            ship_location=input(f'{player}, Wrong location selected, Enter location again: ')                                   # input the location value again      
        
        a = int(ship_location)                                                                                                  # str value of the location converted into integer
        b = a + 10                                                                               
        c = b + 10
        x= str(a)                                                                                                               # integer value again converted into string value
        y=str(b)
        z=str(c)

        if player==player1:                                                                                                    # for player 1 location
            player1_list = [x,y,z]                                                                                             # player 1 ship location 
            print(player1_list)
        else:
            player2_list = [x,y,z]                                                                                             # player 2 ship location
            print(player2_list)                                                                                                

    elif direction=='h':                                                                                                       # if direction is horizontal                                                                
        while ship_location in exempt_list1:                                                                                   # if the input location is in exempt list 1
            ship_location=input(f'{player}, Wrong location selected, Enter the location again: ')                              # Enter the location again

        a = int(ship_location)
        b = a + 1
        c = b + 1
        x = str(a)
        y = str(b)
        z = str(c)
    
        if player==player1:
            player1_list = [x,y,z]
            print(player1_list)
        else:
            player2_list = [x,y,z]
            print(player2_list)
    else:
        set_ship_location(player,input(f'Wrong ship direction Entered, Enter Direction again, h/v: '),board)          # if the user input the location other than h/v then the user have to put the location again
 
f = open('ship_game1.txt','w')                                                                                           # text file is created for the data entry
player1=input("Enter Player 1 name: ")                                                                                # player 1 name entry        
f.write('Enter Player 1 Name: ' + str(player1))                                                                       # player 1 data entry is written in text file
f.write("\n")                                          
f.close()                                                                                                             # text file is closed
                                                                                                                    
player1_direction=input(player1+', '+"Enter your Ship Direction, h/v: ")                                              # player 1 direction entry
player1_board=copy.deepcopy(matrix)                                                                                   # deep copy function is used for coping of the matrix
set_ship_location(player1,player1_direction,player1_board)                                                            # calling of set_ship_location function

f = open('ship_game1.txt','a')
player2=input("Enter Player 2 name: ")                                                                                # player 2 name entry
f.write('Enter player 2 Name: '+ str(player2))  
f.write("\n")
f.close()    
                                                                             
player2_direction=input(player2+', '+"Enter your Ship Direction, h/v: ")                                              # player 2 direction entry 
player2_board= copy.deepcopy(matrix)                                                                                  # deep copy function is used for coping the matrix
set_ship_location(player2,player2_direction,player2_board)

def bombing_ship(player,player_list):                                                                                 # bombing function is for the bomb entry
                                                                                                                          
    global player1_board
    global player2_board
    global list1
    global list2

    bombing_entry=input(f'{player}, Enter your bombing entry: ')                                                    # bomb location entered by the user
     
    destroyed=False                                                                          
  
    if bombing_entry in player_list:                                                                                # if the bombing entry is in the location of the ship
        print ("HIT!!")                                                                                             # if found, then print HIT!
        player_list.remove(bombing_entry)                                                                           # the matched entry is removed from the players list
         
        if not len(player_list):                                                                                    # if no element is remaining in the player list
            destroyed=True                                                                                          # return true                                  

        if destroyed==True:
            f = open('ship_game1.txt','a')
            print(f"Target Destroyed Completely !!!, {player} Wins")                                               # if no element is remaining in the list then target is completely destroyed
            f.write(f'Target Destroyed Completely!!!, {player} Wins')  
            f.write('\n')
            print()
            f.close()                                                                                              # if no element is remaining in the list then target is completely destroyed
            return True                                                        
    else:
        print ("MISS!!")                                                                                            # if bombing entry is not found in the player list then print MISS!!
        list1=[]                                                                                                    # initially list 1 is empty for player 1 for storing the missed bombing entry
        list2=[]                                                                                                    #  player 2 empty list for storing the missed bombing entry for player 2
        if player==player1:                                                                                         # if player1 is assigned in player                                                                    
            list1.append(bombing_entry)                                                                             # missed bombing entry is append in the list1
            print(list1)
            return False           
        else:                                                                     
            list2.append(bombing_entry)                                                                            # initially list 2 is empty for player 2 for storing the missed bombing entry
            print(list2) 
            return False
count=0  
win=False       
player = player1                                                                                                  # for player1 turn 
player_list=player2_list                                                                                          # player2_list is equal to player_list     
                                                                                                                                            
while not win:                                                                                                    # if the player is not equal to True i.e, equal to false                                                        
    win=bombing_ship(player,player_list)                                                                          # calling of bombing_ship function     
    if player==player1:                                                                                           # for player1 turn 
        f = open('ship_game1.txt','a')                                                                               
        count=count+1                                                                                             # for each round, 1 is incremented in the count
        f.write('Number of rounds: ' +str(count))                                                                 # the number of rounds is written in the text file
        f.write("\n")
        f.close()                                                                                                
        player=player2                                                                                            # in the next loop player 2 turn
        player_list=player1_list                                                                                  # now player1_list is assigned to player_list
    else:
        player=player1                                                                                            # player1 is assigned to player
        player_list=player2_list                                                                                  # else,player2_list is assigned to player_list        
    



     
