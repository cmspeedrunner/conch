import os
import colorama
import sys
import webbrowser
import wikipedia

def greeting():
    print(colorama.Fore.BLUE+"Welcome to Conch, type in \"conch help\" for information."+colorama.Fore.WHITE)

def goodbye():
    print(colorama.Fore.BLUE+"Thank "+colorama.Fore.MAGENTA+"you"+colorama.Fore.GREEN+" for"+colorama.Fore.RED+" using "+colorama.Fore.YELLOW+"C"+colorama.Fore.CYAN+"o"+colorama.Fore.GREEN+"n"+colorama.Fore.MAGENTA+"c"+colorama.Fore.BLUE+"h"+colorama.Fore.RESET+"!")

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
    print(colorama.Fore.GREEN+"conch task"+colorama.Fore.WHITE+"- This is how you can open up a task manager window through conch")
    print(colorama.Fore.GREEN+"conch ls"+colorama.Fore.WHITE+"- This is how you can list the contents in the current directory")

greeting()
Loop = True
while Loop == True:
    mainline = input(colorama.Fore.MAGENTA+os.getcwd()+"->"+colorama.Fore.WHITE)
    mainline = mainline.strip()
    if "conch" not in mainline:
        os.system(mainline)

    if mainline == "conch":
        greeting()

    if mainline == "conch ":
        greeting()

    if mainline == "conch help":
        help()
    if mainline == "conch ls":
        os.system("dir /s /b /o:gn")
    if mainline == "conch cpu":
        os.system("wmic cpu get NumberOfCores,NumberOfLogicalProcessors.")
    if mainline == "conch vers":
        version()
    if "conch read" in mainline:
        path = mainline.split("conch read")[1]
        path = path.strip()
        with open(path) as f:
            contents = f.read()
        print(contents)
    if "conch url" in mainline:
        path = mainline.split("conch url")[1]
        path = path.strip()
        webbrowser.open(path)
    if "conch search" in mainline:
        path = mainline.split("conch search")[1]
        path = path.strip()
        webbrowser.open(path)
    if "conch task" in mainline:
        os.system("taskmgr")
        
        os.system("python conch.py")
    if "conch wiki" in mainline:
        path = mainline.split("conch wiki")[1]
        path = path.strip()
        try:
             print(wikipedia.summary(path, auto_suggest=False))
        except(wikipedia.DisambiguationError):
             print(colorama.Fore.BLUE+"\nYour search was too broad, you need to narrow it down.\n"+colorama.Fore.WHITE)
        except(wikipedia.PageError):
             print(colorama.Fore.BLUE+"\nPage not found in database.\n"+colorama.Fore.WHITE)
    if mainline == "conch break":
        goodbye()
        Loop = False
        quit()
        exit()
