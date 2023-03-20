# not working might implement into one source file

import time
import os

debug = 1
autosave = 1

def launcher():
    global launcheropt
    print("""Game Launch menu

    1) Continue Saved Game
    2) New Game
    3) Settings 
    4) Exit
    """.center(50))
    launcheropt = input("")

def settings():
    global debug, autosave
    settingsopt = input("")
    if settingsopt == "1":
        if debug == 1:
            debug = 0
            print("\nDebug mode disabled")
        elif debug == 0:
            debug = 1
            print("\nDebug mode enabled")
    elif settingsopt == "2":
        if autosave == 1:
            autosave = 0
            print("\nAuto save disabled")
        elif autosave == 0:
            autosave = 1
            print("\nAuto save enabled")
    else:
        print("Invalid option")
        time.sleep(1)
        os.system("cls")
        launcher()

launcher()
if launcheropt == "1":
    savefile = input("\nEnter character name: ")
    if savefile+ ".bun" in os.listdir("./save/"):
        print("Loading save file...")
        time.sleep(2)
        # load save file
        print("Continuing Saved Game")
    else:
        print("Save file not found")
        time.sleep(1)
        os.system("cls")
        launcher()
elif launcheropt == "2":
    print("Starting new game...")
    time.sleep(2)
    # start new game
elif launcheropt == "3":
    print("\nSettings")
    print("""\n1) Enable/disable Debug mode (not implemented, disabled by default)
    2) Enable/disable Auto save (not implemented, enabled by default)
    """)
    settings()
elif launcheropt == "4":
    print("Exiting...")
    time.sleep(1)
    exit(0)


