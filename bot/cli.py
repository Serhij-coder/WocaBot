import os
import sys
from time import sleep

WHITE = "\033[97m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def choseMode(config):
    mode = None
    debug("Enter mod choosing func", config)
    while True:
        if config["mode"] == "0":
            info("Chose program mode")
            info("------------")
            info("[1] Do all uncompleted packages")
            info("[2] Do training")
            info("[3] Is it test today")
            info("------------")
            mode = input("Chose mode (number): ")
        else:
            info("Mode is defined in config.json")
            mode = config["mode"]
        debug(f"Chosen mode: {mode}", config)
        if mode != "1" and mode != "2" and mode != "3":
            clear_console()
            error("Invalid mode")
            info("Chose 1, 2 or 3")
            continue
        else:
            success(f"Mode chosen: {mode}")
            break

    return mode

def choseTestMode(config):
    mode = None
    debug("Enter test mod choosing func", config)
    while True:
        if config["testMode"] == "0":
            info("Chose test mode")
            info("------------")
            info("[1] Semi automatic")
            info("[2] Automatic (doesn't work yet)")
            info("------------")
            mode = input("Chose mode (number): ")
        else:
            info("Mode is defined in config.json")
            mode = config["testMode"]
        debug(f"Chosen mode: {mode}", config)
        if mode != "1" and mode != "2":
            clear_console()
            error("Invalid mode")
            info("Chose 1 or 2")
            continue
        else:
            if mode == "2":
                clear_console()
                error("Automatic mode doesn't work yet")
                info("Please use semi automatic mode")
                # warning("Use it at your own risk")
                # a = input("Do you want to continue? (y/N) ")
                # if a.lower() != "y":
                continue
            success(f"Mode chosen: {mode}")
            break

    return mode

def controleAllFiles():
    files = [
        "config.json",
    ]

    missing_files = [f for f in files if not os.path.exists(f)]

    if missing_files:
        error("Missing necessary files")
        info("Read README for installation instructions")
        sys.exit(1)
    else:
        success("All files found")

def erase_last_line():
    print("\033[A\033[K", end="")  # Move cursor up and clear the line

def clear_console():
    print("\033[H\033[J", end="")  # Clears the screen and moves the cursor to the top-left

def info(msg): print(f"{WHITE}{msg}{RESET}")
def error(msg): print(f"{RED}[ERROR] {msg}{RESET}")
def debug(msg, conf):
    if conf["isDebug"]:
        print(f"{YELLOW}[DEBUG] {msg}{RESET}")
def success(msg): print(f"{GREEN}[OK] {msg}{RESET}")
def warning(msg): print(f"{YELLOW}[WARNING] {msg}{RESET}")

iter = True
def warnBlink():
    global iter
    ascii_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠿⠿⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⢡⠀⠀⠀⠀⠀⢀⡈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢠⣿⠀⠀⠀⠀⠀⢸⣷⡈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⢀⣼⠏⢠⣿⣿⡆⠀⠀⠀⠀⣸⣿⣷⡄⠹⣆⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⢀⣾⠃⣰⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⡄⠹⣷⡀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⢠⡿⠁⣰⣿⣿⣿⣿⣿⠀⠀⠀⢠⣿⣿⣿⣿⣿⣆⠘⣷⡀⠀⠀⠀⠀
     ⠀⠀⠀⢠⡿⠁⣼⣿⣿⣿⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣆⠘⢿⡄⠀⠀⠀
     ⠀⠀⣠⡟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠈⢿⡄⠀⠀
     ⠀⢰⡿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣿⡄⠀
     ⠀⢼⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢸⡇⠀
     ⠀⠘⣷⣄⠙⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⣠⡿⠃⠀
     ⠀⠀⠈⠉⠛⠓⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    text = """
 _____  ________   ________  _____  ____  
|  __ \|  ____\ \ / /  ____|/ ____|/ __ \ 
| |__) | |__   \ V /| |__  | (___ | |  | |
|  ___/|  __|   > < |  __|  \___ \| |  | |
| |    | |____ / . \| |____ ____) | |__| |
|_|    |______/_/ \_\______|_____/ \____/ 
   """

    if iter:
        clear_console()
        print(YELLOW + ascii_art + RESET)
        print(RED + text + RESET)
        sleep(0.2)
        clear_console()
        iter = False
    else:
        sleep(0.2)
        iter = True