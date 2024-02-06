from termcolor import colored #used to change output text color

Player1Health,Player2Health = 100,100 

CurrentMove = 1

def UI(CPN,CPH,CM):
  print("========================================================")
  print("                                .--_ ......._-_--.      ")
  print("                               (|\ /      / /| \  \     ")
  print("                               /  /     .'  -=-'   `.   ")  
  print("    "+str(CPN)+"'s Turn!"+"              /  /    .'             )  ")  
  print("                            _/  /   .'        _.)   /   ")
  print("                           / o   o        _.-' /  .'    ")  
  print("                           \          _.-'    / .'*|    ")        
  print("    HP:"+ColorChange(CPH)+"                  \______.-'//    .'.' \*|  ")
  print("                             \|  \ | //   .'.' _ |*|    ")   
  print("                              `   \|//  .'.'_ _ _|*|    ")
  print("                               .  .// .'.' | _ _ \*|    ")
  print("    CurrentTurn:"+colored(str(CM),"light_yellow")+"              \`-|\_/ /    \ _ _ \*\\   ")
  print("                                `/'\__/      \ _ _ \*\\  ")
  print("                                /^|           \ _ _ \*\\ ")
  print("                               '  `            \ _ _ \*\\") 
  print("=========================================================")
  return "" #took an hour to debug

Player1Name = colored(input("Player 1 Enter Name: "),"red")
Player2Name = colored(input("Player 2 Enter Name: "),"blue")

Player1AttackPower,Player2AttackPower = 1,1  #defining variables

Player1Status,Player1Buff,Player1DeBuff = 0,0,0
Player2Status,Player2Buff,Player2Debuff = 0,0,0

#low attack damage base move

def Bite(CurrentMove):
    global Player1Health, Player2Health
    if CurrentMove % 2 != 0:
        print("\n" + Player1Name + " Bites " + Player2Name + "...")
        Player2Health = Player2Health - (16 * Player1AttackPower)
        print("\n" + "for " + str(16 * Player1AttackPower) + " damage ["+Player2Name+"'s HP:" + ColorChange(Player2Health+(16 * Player1AttackPower)) + " -> " + ColorChange(Player2Health) +"]\n")
    elif CurrentMove % 2 == 0:
        print("\n" + Player2Name + " Bites " + Player1Name + "...")
        Player1Health = Player2Health - (16 * Player2AttackPower)
        print("\n" + "for " + str(16 * Player2AttackPower) + " damage ["+Player1Name+"'s HP:" + ColorChange(Player1Health+(16 * Player2AttackPower)) + " -> " + ColorChange(Player1Health) +"]\n")

#Next turn other player does -100% damage

def Constrict(CurrentMove):
    global Player1Health, Player2Health, Player2Debuff, Player1DeBuff
    if CurrentMove % 2 != 0:
        print("\n" + Player1Name + " Constricts " + Player2Name)
        Player2Debuff = 1
        print("\n" + "for next turn ["+Player2Name+"'s AP:" + str(Player2AttackPower) + " -> 0]")
    elif CurrentMove % 2 == 0:
        print("\n" + Player2Name + " Constricts " + Player1Name)
        Player1DeBuff = 1
        print("\n" + "for next turn ["+Player1Name+"'s AP:" + str(Player1AttackPower) + " -> 0]")

#Player loses 10 hp then gains +100% attack damage

def Shed(CurrentMove):
    global Player1Health, Player2Health, Player1Buff, Player2Buff
    if CurrentMove % 2 != 0:
        print("\n" + Player1Name + " uses Shed" + "...")
        Player1Health = Player1Health - 10
        Player1Buff = 1
        print("\n" + "for 10 self inflicted damage ["+Player1Name+"'s HP:"+ ColorChange(Player1Health+10) + " -> " + ColorChange(Player1Health) +"] and ["+Player1Name+"'s AP:" + str(Player1AttackPower) + " -> 2]\n")
    elif CurrentMove % 2 == 0:
        print("\n" + Player2Name + " uses Shed " + "...")
        Player2Health = Player2Health - 10
        Player2Buff = 1
        print("\n" + "for 10 self inflicted damage ["+Player2Name+"'s HP:"+ ColorChange(Player2Health+10) + " -> " + ColorChange(Player2Health) +"] and ["+Player2Name+"'s AP:" + str(Player2AttackPower) + " -> 2]\n")
        

#Apply poison for 3 turns

def Fang(CurrentMove):
    global Player1Health, Player2Health, Player1Status, Player2Status
    if CurrentMove % 2 != 0:
        print("\n" + Player1Name + " sinks venom into " + Player2Name)
        Player2Status += 3
        print("\n" + "for next " + str(Player2Status) + " turns ["+Player2Name+"'s STAT:" + str(Player2Status-3) + " -> " + str(Player2Status)+" Poison]")
    elif CurrentMove % 2 == 0:
        print("\n" + Player2Name + " sinks venom into " + Player1Name)
        Player1Status += 3
        print("\n" + "for next " + str(Player1Status) + " turns ["+Player1Name+"'s STAT:" + str(Player1Status-3) + " -> " + str(Player1Status)+" Poison]")

Moves = {"Bite":Bite, "Constrict":Constrict, "Shed":Shed, "Fang":Fang}

def ColorChange(i):    #used to change color of health percentages
  if i > 66:
    return colored(str(i),"green")
  if i > 33 and not i > 66:
    return colored(str(i),"light_yellow")
  if i < 33:
    return colored(str(i),"red")

print("\nPlease choose one of the following moves:\n"+(colored("Bite","magenta"))+"\nDeal 16 damage to opponent, can be effected by both buffs and debuffs\n"+(colored("Constrict","magenta"))+"\nCancel out opposing player following attack damage essentially a 0X damage debuff\n"+(colored("Fang","magenta"))+"\nApplies status effect poison for next three turns on opponent dealing 9 damage each turn\n"+(colored("Shed","magenta"))+"\n10 self inflicted damage followed by a 2X damage buff for the following turn\n",) 

GameLoop = True    #main game loop to keep track of current turns and function call when applicable
while GameLoop:
    if CurrentMove % 2 != 0:          #first player
        if Player1Health <= 0:        #ends game when health is less than equal to 0
          print("\n" + "Game Over " + Player2Name + " Wins!")
          break
        print(UI(Player1Name,Player1Health,CurrentMove))      #color change 
        if Player1Status > 0:         #keeps track the fang function
          Player1Health -= 9
          Player1Status -= 1
          print("*poison damage* \n\n[" + Player1Name + "'s HP:" + ColorChange(Player1Health + 9) + " -> " + ColorChange(Player1Health) + "] and [" + Player1Name + "'s STAT:" + str(Player1Status+1) + " -> " + str(Player1Status) + ' Poison]\n')
          if Player1Status == 0:
            print("*poison dissipated\n")
        if Player1Buff > 0:
          Player1AttackPower = 2
          print("*2X buff in effect*\n")
          Player1Buff -= 1
        if Player1DeBuff > 0:
          Player1AttackPower = 0
          print("*0X debuff in effect*\n")
          Player1DeBuff -= 1
        input_move_p1 = input(Player1Name + " pick a move: ")                  #makes sure input can correctly call function regardesss of upper/lower case
        input_move = (input_move_p1[0].upper()) + (input_move_p1[1:].lower())
        if input_move not in ["Bite","Shed","Fang","Constrict"]:               #makes sure user inputs a valid input
            print("\nPlease choose one of the following moves:\n\n"+(colored("Bite, ","magenta"))+(colored("Constrict, ","magenta"))+(colored("Fang, ","magenta"))+(colored("Shed ","magenta")+"\n")) 
            continue
        Moves[input_move](CurrentMove)
        CurrentMove += 1
    elif CurrentMove % 2 == 0:                                      #player 2 (same as first player)
        if Player1Health <= 0:
          print("\n" + "Game Over " + Player1Name + " Wins!")
          break
        print(UI(Player2Name,Player2Health,CurrentMove))
        if Player2Status > 0:
          Player2Health -= 9
          Player2Status -= 1
          print("*poison damage* \n\n[" + Player2Name + "'s HP:" + ColorChange(Player2Health + 9) + " -> " + ColorChange(Player2Health) + "] and [" + Player2Name + "'s STAT:" + str(Player2Status+1) + " -> " + str(Player2Status) + ' Poison]\n')
          if Player2Status == 0:
            print("*poison dissipated\n")
        if Player2Buff > 0:
          Player2AttackPower = 2
          print("*2X buff in effect*\n")
          Player2Buff -= 1
        if Player2Debuff > 0:
          Player2AttackPower = 0
          print("*0X debuff in effect*\n")
          Player2Debuff -= 1
        input_move_p2 = input(Player2Name + " pick a move: ")
        input_move2 = (input_move_p2[0].upper()) + (input_move_p2[1:].lower())
        if input_move2 not in ["Bite","Shed","Fang","Constrict"]:
          print("\nPlease choose one of the following moves:\n\n"+(colored("Bite, ","magenta"))+(colored("Constrict, ","magenta"))+(colored("Fang, ","magenta"))+(colored("Shed ","magenta")+"\n"))
          continue
        Moves[input_move2](CurrentMove)
        CurrentMove += 1
