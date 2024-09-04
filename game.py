import random
import time

def print_sleep(message, wait_time=0):
    """Prints a message and waits for a specified amount of time."""
    print(message)
    time.sleep(wait_time)


def play_again():
    """Asks the player if they want to play again."""
    choice=''
    while choice not in ['n','y']:
        choice = input("Would you like to play again? (y/n)") 
    
    if choice == 'n':
        print_sleep("Thanks for playing! See you next time.", 2)
        return 'game_over'
    elif choice == 'y':
        print_sleep("Great! Restarting the adventure...", 2)
        return 'explore'


def intro():
    print_sleep("You find yourself on a deserted island after your ship wrecked.",3)
    print_sleep("The island is known for its hidden treasures, but also for its dangers.",3) 
    print_sleep("You need to find a way off the island or discover the hidden treasure!",2)
    print_sleep("You see two paths ahead:",2)


def where_to():
    """Player chooses to either escape or attempt an engine repair."""
    print_sleep("1. Activate Escape option", 2)
    print_sleep("(Eject Immediately)")
    print_sleep("2. Attempt Main Engine Repair", 2)
    print_sleep(" (Risky, but may allow for controlled landing)")
    print_sleep("", 3)
    
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        choose_path()
    elif choice == '2':
        attempt_engine_repair()


def choose_path():
    """Player chooses between two paths."""
    print_sleep("\n1. The Path to the Ancient Ruins",2)
    print_sleep("2. The Path to the Dark Forest",2)

    choice=''
    while choice not in ['1','2']:
        choice = input("Which path will you choose? (1 or 2)\n")
        
    
    if choice == '1':
        ancient_ruins()
    elif choice == '2':
        dark_forest()
    




def attempt_engine_repair():
    """Scenario if the player chooses to attempt an engine repair."""
    print_sleep("you work hard unsure if your efforts will be enough", 2)
    print_sleep("you find the problem complex")
    
    choice = ''
    while choice not in ['1', '2']:
        choice = input("Do you: 1. Follow the manual step-by-step or 2. Try a risky shortcut? (1 or 2):\n")
    
    if choice == '1':
        if ASSISTANCE == "fixer":
            print_sleep("You call up the fixer and he helps you.", 2)
            print_sleep("Soon, help arrives, and you are saved. Congratulations, you win!", 2)
        else:
            print_sleep(f"You call the {helper}, but there's no one to help you.", 2)
            print_sleep("Unfortunately, it doesn't work. Back to choices.", 2)
            where_to()
            
    elif choice == '2':
        if random.choice([True, False]):
            print_sleep("Initially, it seems to work, but suddenly the engines explode.", 2)
            print_sleep("You are caught in the explosion and do not survive. Unfortunately, you lose.", 2)
        else:
            print_sleep("You managed to stabilize the engines and control the landing. You win!", 2)



def  ancient_ruins():
    """The scenario if the player chooses the Ancient Ruins."""
    print_sleep("You arrive at the ancient ruins. The place is eerily quiet.",2)
    print_sleep("You notice a strange marking on the wall.",2)

    choice=''
    while choice not in ['1','2']:
        choice = input("""
    Do you:
    1. Touch the marking
    2. Ignore it and search for another clue (1 or 2):
    """)
    

    if choice == '1':
        if random.choice([True, False]):
            print_sleep("The marking glows and reveals a hidden treasure! You have found the legendary treasure of the island. You win!", 2)
        else:
            print_sleep("The marking triggers a trap and the ruins start to collapse! You are trapped under the rubble and do not survive. You lose.", 2)
    elif choice == '2':
        if random.choice([True, False]):
            print_sleep("You find an ancient map leading to hidden treasure! Following the map, you discover a chest full of gold. You win!", 2)
        else:
            print_sleep("Suddenly, the ground beneath you collapses! You fall into a deep pit and are trapped. Unfortunately, you lose.", 2)


def dark_forest():
    """The scenario if the player chooses the Dark Forest."""
    print_sleep("You enter the dark forest. The trees are tall and the light is dim.",2)
    print_sleep("You hear strange noises coming from deep within the forest.",2)
    choice=''
    while choice not in ['1','2']:
        choice=input("""
    Do you:
    1. Investigate the noises
    2. Find a place to hide and wait (1 or 2):
    """)
        
        
    if choice == '1':
        if random.choice([True, False]):
            print_sleep("You bravely investigate the noises and find a hidden cave. Inside, you discover a small chest filled with gold coins. You win!", 2)
        else:
            print_sleep("You find a dangerous wild animal instead! You try to escape but are caught. Unfortunately, you lose.", 2)
    elif choice == '2':
        if random.choice([True, False]):
            print_sleep("You hide behind a tree and the noises fade away. After waiting, you safely leave the forest and find a rescue team. You win!", 2)
        else:
            print_sleep("You hide behind a tree, but the noises get closer. Suddenly, a wild animal jumps out and you are unable to escape. You lose.", 2)



GAME_STATE = 'explore'

while GAME_STATE == 'explore':
    sos = ['doctor', 'fixer', 'teacher', 'farmer']
    helper = random.choice(sos)
    ASSISTANCE = 'fixer'
    
    intro()
    where_to()
    GAME_STATE=play_again()