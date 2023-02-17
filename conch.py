import os
import colorama
import sys
import webbrowser
import wikipedia
import random

def tictac():
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

    board_keys = []

    for key in theBoard:
        board_keys.append(key)



    def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
    def game():

        turn = colorama.Fore.MAGENTA+'X'+colorama.Fore.RESET
        count = 0


        for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ". Move to which place? (1-9)")

            move = input()        

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count = count
            else:
                print("That place is already filled.\nMove to which place?")
                continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")                
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                    printBoard(theBoard)
                    print("\nGame Over.\n")                
                    print(" **** " +turn + " won. ****")
                    break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")

        # Now we have to change the player after every move.
            if turn == colorama.Fore.MAGENTA+'X'+colorama.Fore.RESET:
                turn = colorama.Fore.BLUE+'O'+colorama.Fore.RESET
            else:
                turn = colorama.Fore.MAGENTA+'X'+colorama.Fore.RESET      
    
    # Now we will ask if player wants to restart the game or not.
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":  
            for key in board_keys:
                theBoard[key] = " "

            game()

    if __name__ == "__main__":
        game()

def greeting():
    print(colorama.Fore.BLUE+"Welcome to Conch, type in \"conch help\" for information."+colorama.Fore.WHITE)

def goodbye():
    text = "Thank you for using Conch!"
    colored_text = [getattr(colorama.Fore, f"{random.choice(list(colorama.Fore.__dict__.keys())[1:])}") + char + colorama.Fore.RESET for char in text]
    print(''.join(colored_text))
def version():
    print(colorama.Fore.BLUE+"""
       /\\
      {.-}
     ;_.-'\\
    {    _.}_
     \.-' /  `,
      \  |    /
       \ |  ,/
        \|_/   
CONCH                 
VERSION: ALPHA V/0.5
LICENSE: OPEN SOURCE
DEV: CmSpeedrunner
GITHUB: https://github.com/cmspeedrunner/conch              """+colorama.Fore.WHITE)

def help():
    print(colorama.Fore.BLUE+"CONCH COMMANDS:"+colorama.Fore.WHITE)
    print(colorama.Fore.BLUE+"------------------------------------------------------------"+colorama.Fore.WHITE)
    print(colorama.Fore.GREEN+"conch vers"+colorama.Fore.WHITE+"- This will show the version and details about the version of conch you are running.")
    print(colorama.Fore.GREEN+"conch cpu"+colorama.Fore.WHITE+"- This will show the cpu's running and operating alongside conch.")
    print(colorama.Fore.GREEN+"conch break"+colorama.Fore.WHITE+"- This is the escape/exit key and withh break from conch.")
    print(colorama.Fore.GREEN+"conch read"+colorama.Fore.WHITE+"- This is how you can read and echo a files contents. Just enter the path after \"conch read\"")
    print(colorama.Fore.GREEN+"conch url"+colorama.Fore.WHITE+"- This is how you can open a website url through conch, just enter the URL after \"conch url\"")
    print(colorama.Fore.GREEN+"conch wiki"+colorama.Fore.WHITE+"- This is how you can get a wikipedia page through conch, just enter the topic after \"conch wiki\"")
    print(colorama.Fore.GREEN+"conch search"+colorama.Fore.WHITE+"- This is how you can search a web browser for a question or any query you have, just enter your query after \"conch search\"")
    print(colorama.Fore.GREEN+"conch task"+colorama.Fore.WHITE+"- This is how you can print out quickly the tasks you are running through conch")
    print(colorama.Fore.GREEN+"conch ls"+colorama.Fore.WHITE+"- This is how you can list the contents in the current directory")
    print(colorama.Fore.GREEN+"conch net"+colorama.Fore.WHITE+"- This will display all network details about the networks and ips on your computer.")
    print(colorama.Fore.GREEN+"conch profile"+colorama.Fore.WHITE+"- This will display your computer profile")
    print(colorama.Fore.GREEN+"conch copy"+colorama.Fore.WHITE+"- This will copy everything from one file to another, for example: \"conch copy from_folder to_folder\"")
    print(colorama.Fore.GREEN+"conch shutdown"+colorama.Fore.WHITE+"- This will shutdown your pc immediately, use if something is broken or frozen.")    
    print(colorama.Fore.GREEN+"conch error"+colorama.Fore.WHITE+"- This displays the most recent critical and error events from the System event log.")
    print(colorama.Fore.GREEN+"conch disk"+colorama.Fore.WHITE+"- This will open up the disk managment dialog.")
    print(colorama.Fore.GREEN+"conch sysconfig"+colorama.Fore.WHITE+"- This will open up the system configuration gui.")
    print(colorama.Fore.GREEN+"conch tictac"+colorama.Fore.WHITE+"- This will open up a 2 player tictactoe game, where you enter a number from 1,9 to place crosses or circles")
    print(colorama.Fore.GREEN+"conch battery"+colorama.Fore.WHITE+"- This will create and generate a battery report as a .html file and open it.")
conch_commands = [
    "conch",
    "conch help",
    "conch vers",
    "conch cpu",
    "conch break",
    "conch read",
    "conch url",
    "conch wiki",
    "conch search",
    "conch task",
    "conch ls",
    "conch net",
    "conch profile",
    "conch copy",
    "conch shutdown",
    "conch error",
    "conch disk",
    "conch sysconfig",
    "conch tictac",
    "conch battery"
]

greeting()
Loop = True
while Loop == True:
    mainline = input(colorama.Fore.MAGENTA+os.getcwd()+"->"+colorama.Fore.WHITE)
    mainline = mainline.strip()
    if "conch" not in mainline:
        os.system(mainline)

    if mainline == "conch":
        greeting()
    if mainline == "conch tictac":
        tictac()

    if mainline == "conch help":
        help()
    if mainline == "conch ls":
        os.system("dir /s /b /o:gn")
    if mainline == "conch cpu":
        os.system("wmic cpu get NumberOfCores,NumberOfLogicalProcessors.")
    if mainline == "conch vers":
        version()
    if mainline == "conch battery":
        os.system("powercfg /batteryreport /output \"""C:\\Users\\User\\battery-report.html""\"")
        os.startfile("C:\\Users\\User\\battery-report.html")
    if "conch read" in mainline:
        path = mainline.split("conch read")[1]
        path = path.strip()
        with open(path) as f:
            contents = f.read()
        print(contents)
    if "conch net" in mainline:
        os.system("netstat -an")
        os.system("ipconfig /all")
    if "conch sysconfig" in mainline:
        os.system("msconfig")
    if "conch url" in mainline:
        path = mainline.split("conch url")[1]
        path = path.strip()
        webbrowser.open(path)
    if "conch search" in mainline:
        path = mainline.split("conch search")[1]
        path = path.strip()
        webbrowser.open(path)
    if "conch copy" in mainline:
        from2 = mainline.split()
        from2 = from2[2]    

        to2 = from2[3]
        os.system("xcopy "+"\""+from2+"\"" + " \""+to2+"\""+" /e /i /h /y")
    if mainline == "conch task":
        os.system("tasklist")
    if mainline == "conch disk":
        os.system("diskmgmt.msc")
    if mainline == "conch error":
        os.system("wevtutil qe System /rd:true /f:text /c:1 /q:\"*[System[(Level=1 or Level=2)]]\"")
    if mainline == "conch shutdown":
        os.system("shutdown /s /t 0")
    if mainline == "conch profile":
        os.system("systeminfo")
        os.system("whoami /user")
    if "conch compare" in mainline:
        os.system("comp")
    if "conch wiki" in mainline:
        path = mainline.split("conch wiki")[1]
        path = path.strip()
        try:
             print(wikipedia.summary(path, auto_suggest=False))
        except(wikipedia.DisambiguationError):
             print(colorama.Fore.BLUE+"\nYour search was too broad, you need to narrow it down.\n"+colorama.Fore.WHITE)
        except(wikipedia.PageError):
             print(colorama.Fore.BLUE+"\nPage not found in database.\n"+colorama.Fore.WHITE)
    if "conch" in mainline and mainline not in conch_commands:
        listofmain = mainline.split("conch")[1]
        listofmain = listofmain.strip()
        print(colorama.Back.RED+"No conch command with name of: '"+listofmain+"'"+colorama.Back.RESET)
        print(colorama.Back.RED+"Try 'conch help' to see a list of the avalible commands"+colorama.Back.RESET)
    if mainline == "conch break":
        goodbye()
        Loop = False
        quit()
