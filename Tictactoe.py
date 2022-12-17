print("Welcome to Your favourite childhood game Tic Tac Toe.")
print('''Instructions to play the game are as follows:
        There are 9 Boxes which represent the positions, as a user you just need to enter the 
        box number.  
        Picture represent the positions of Box Number:
        [1,2,3]
        [4,5,6]
        [7,8,9]
        "O" represnts Player1 and "X" represents Player2.''')
print()
Player1 = input("Name of Player one: ")
Player2 = input("Name of Player two: ")
Start = True
while(Start):
    Tic_tac_toe = [[" "," "," "],[" "," "," "],[" "," "," "]]
    count = 0
    while(count<9):

        if count%2 == 0:
            Box_Number = int(input(Player1+" "+"Enter the Box Number: "))
            print()
        else:
            Box_Number = int(input(Player2+" "+"Enter the Box Number: "))
            print()
        if Box_Number>0 and Box_Number<=9:
        
            if Box_Number == 1:
                row,col = 0,0
            elif Box_Number == 2:
                row,col = 0,1
            elif Box_Number == 3:
                row,col = 0,2
            elif Box_Number == 4:
                row,col = 1,0
            elif Box_Number == 5:
                row,col = 1,1
            elif Box_Number == 6:
                row,col = 1,2
            elif Box_Number == 7:
                row,col = 2,0
            elif Box_Number == 8:
                row,col = 2,1
            else:
                row,col = 2,2

            if Tic_tac_toe[row][col] != " ":
                print("Box is already filled Choose another Box.")
                print()
            else:
                if count%2 == 0:
                    Tic_tac_toe[row][col] = "O"
                else:
                    Tic_tac_toe[row][col] = "X"
                
                if Box_Number == 1:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row+2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row+2][col+2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break

                    
                elif Box_Number == 2:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row+2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            break
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                            break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")

                elif Box_Number == 3:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row+2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col-2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row+2][col-2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                elif Box_Number == 4:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break

                elif Box_Number == 5:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col-1]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col+1]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                
                elif Box_Number == 6:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row+1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col-2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                
                elif Box_Number == 7:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col+1] and Tic_tac_toe[row][col] == Tic_tac_toe[row-2][col+2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                
                elif Box_Number == 8:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col+1]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                
                elif Box_Number == 9:
                    if Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col] and Tic_tac_toe[row][col] == Tic_tac_toe[row-2][col]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                            
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row][col-2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                    elif Tic_tac_toe[row][col] == Tic_tac_toe[row-1][col-1] and Tic_tac_toe[row][col] == Tic_tac_toe[row-2][col-2]:
                        if count%2 == 0:
                            print("Hurray!"+","+Player1,"Won the match.")
                        else:
                            print("Hurray!"+","+Player2,"Won the match.")
                        break
                print(Tic_tac_toe[0])
                print(Tic_tac_toe[1])
                print(Tic_tac_toe[2])
                print()
                count += 1
        else:
            print("Invalid Box Number,Enter valid Box Number.") 
            print()           
    else:
        print("It is a draw, well played both of you.")
    
    print()
    print("Final Result: ")
    print(Tic_tac_toe[0])
    print(Tic_tac_toe[1])
    print(Tic_tac_toe[2])
    print()
    
    flag = True
    while(flag):
        Decision = input("If you want to play again write START or else EXIT: ").lower()
        print()
        if Decision == "start":
            Start = True
            flag = False
        elif Decision == "exit":
            Start = False
            flag = False
        else:
            print("Invalid entry,Enter only START or EXIT.")
            print()
    

        






        


    


