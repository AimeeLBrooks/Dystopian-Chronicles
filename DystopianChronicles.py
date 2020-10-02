# Important Libraries and Imports (Keep here to keep code clean)
import random
import time
import sys
from threading import Timer

timeout = 10

# END GAME DEF VALUE
def failure():
    time.sleep(1.5)
    print ("You were apprehended.")
def death():
    time.sleep(1.5)
    print ("You died.")
def key():
    print("key")
    time.sleep(1.5)
def idiocy():
    time.sleep(1.5)
    print ("You really should've picked that item up.")

#KEY:
#FOYER
#ROUTE A
#ROUTE B, B1, B2, B3
#ROUTE C
#BOSS BATTLE

#INSTANCES - must be at top for "def" function to work - these must go in REVERSE chronological order as the DEF must be stated. The codes are listed in CHRONOLOGICAL order at the foorter of this sheet. 

#BOSS

def ending():
    time.sleep(2)
    print("\nTHANK YOU FOR PLAYING DYSTOPIAN CHRONICLES!")
    time.sleep(1.5)
    print("THIS GAME WAS CREATED BY SHANNON AND AIMÉE")
    exit()

def finalendingb():
    time.sleep(1.5)
    print ("You push down with a great deal of force only to have yourself tossed back by inhuman strength, you reach forward toward a piece of metal glistening in the darkness. He increases his speed, his foot steps growing faster with each passing moment until nothing between you remains but hot breath and the sticky crimson liquid falling off steel. In the darkness you can't tell what you used against him, but as his body falls to the ground and the lights illuminate every corner of the arena you become acutely aware of what's become of you. A thousand watchful eyes from the rafters and pews scattered about the circular arena. This wasn't the removal of the rebellion. This was entertainment.")
    time.sleep(3)
    print("You look up into the eyes of the man sat on the large throne ahead of you. The eyes of your boss. The very man who instructed you to come here in the first place. He smiles evily and gives you a thumbs up.\n\n")
    time.sleep(1.5)
    print("You have completed your mission...\nEven if it was all for nothing....\nit's over")
    ending()

def finalendinga():
    time.sleep(1.5)
    print ("The man grins at you maniacally.")
    time.sleep(1.5)
    print("His smile curves wider and wider until it forms a sinister curve beneath burning eyes.\nYou shiver slightly at his expression as he lunges forward toward you, your first attempt to arm yourself with what weapons you found or even your fist meaning nothing at all against his brute force. Bodies roll and contort beneath the snapping of bones and breaking of skin.\n Nothing but screams echo throughout the halls of the hideout as wires twist through metal and flesh.\n")
    time.sleep(2)
    print("The sound of a gunshot the only sound in memory as all fades to black.  \n") 
    death()

def bossfight():
    time.sleep(1)
    print ("A pair of claws burrow into your neck as hot skin parts red... you begin to wail, throwing your head back as if by instinct causing the body behind to crash to the ground.\nBeneath you lies a dishevelled mound of hair and cotton, then eyes framed by tight ringlets enough to cause sickness to form in the lowest parts of your belly.\n")
    time.sleep(6) 
    print("1) Say his name.\n2) Kick him in the face before he manages to stand.  \n")
    t = Timer(timeout, print, ['He stabbed your in the stomach, causing you to bleed out on the resistence floor.\n You failed your mission. Try again.'])
    t.start()
    prompt = "You have %d seconds to save your life...\nWhat do you do?" % timeout
    print(prompt)
    t.cancel()
    while(1):    
        query = int(input(""))
        if query == 1:  
            time.sleep(1.5)
            print("\n'Gertrude.' You say calmly. ")
            finalendinga()  
        elif query == 2: 
            time.sleep(1.5) 
            print("\nThe heel of your boot causes his nose to crack beneath it's weight as you stop down on his face.")
            finalendingb() 
        else:    
            print ("Pick something.") 
            bossfight()

def route_A5():
    time.sleep(1.5)
    print ("\n\nYou arrive at a rather large pair of crimson doors formed of ancient wood. The width of your palm presses against the bark, causing the air around you to rush forward into the darkerned room illuminated by a single wavering flame in the distance.")
    time.sleep(1.5) 
    bossfight()

# AIMÉE/SHANNON (ROUTE A4)
def route_A4():
    time.sleep(1.5)
    print ("\nYou head into the room on the right, and come across a group of Resistance recruits.")
    time.sleep(1.5) 
    print("They look suspiciously at you and ask who you are.")
    time.sleep(1.5) 
    print("What will you tell them?\n") 
    print("1) I'm a new Resistence initiate. The boss told me to meet here to plan the next attack \n\n2) I don't know, i was just looking for the toilets and must have come the wrong way. Sorry! \n\n3) What do you mean, who am i? I should be asking who are you?! I'm only the second in command here. How dare you insult me with this insolence\n") 
    while(1):    
        query = input("")
        if (query == ("1")): 
            time.sleep(1.5)
            print("\nThe recruits look at you half convinced, half unsure. The biggest of the group stands and towers over you.")
            time.sleep(1.5) 
            print("'Oh yeah?' he says. 'What's the bosses name then?'")
            boss_name = int(input("\nThe boss is called\n\n 1)Greg\n 2)Gerry\n 3)Geraldine\n 4)Gertrude \n"))
            if boss_name == 4:
                time.sleep(1.5)
                print("Hmm, i guess you are a new recruit. You're meant to be in the meeting in 10 minutes. Take a left out of here and you'll find your way")
                time.sleep(1.5)
                print("You thank him and leave the room, wiping your brow at how lucky you are")
                time.sleep(1.5)
                print("You continue down the corridor...")
                route_A5()

            else:   
                print ("Wrong answer kiddo!\n\nThe recruits grab you by the neck and throw you in an interrogation room where they torture you until you lose consciousness") 
                time.sleep(1.5)
                print("\nGAME TERMINATED")
                death()
        if (query == ("2")):  
            time.sleep(1.5)
            print("\nThey grunt at you and you quickly leave the room before you arouse any more suspicion ")
            time.sleep(1.5)
            print("You continue down the corridor...")
            route_A5()
        if (query == ("3")):
            time.sleep(1.5)
            print("Did you really think they'd believe you?")
            time.sleep(1.5)
            print("They lock you in a room which the BOSS should be able to open. You can't.")
            death()

# AIMÉE/SHANNON (ROUTE A35 )
def route_A35():
    time.sleep(1.5)
    print("\nYou enter the room and discover a pile of weapons!/n")
    print("You see a knife, a gun, and an axe \n")
    time.sleep(2)
    print("What do you want to take? (1, 2, 3, 4) \n")
    time.sleep(1)
    print("1) Nothing \n2) Knife \n3) Gun \n4) Axe  \n") #maybe convert to list that removes each weapon each time, maybe? - can be added to final boss fight too!
    while(1):    
        query = int(input(""))
        if query ==1:  
            time.sleep(1.5)
            print("You don't pick up anything??")
            time.sleep(1.5)
            print("Well...\nyou should have done. ")
            route_A4()  
        if query ==2:
            time.sleep(1.5)
            knife_gotten = 1
            print("The blade is sharp with a series of carefully carved runes etched into it's surface.\n")
            time.sleep(1.5) 
            print("It's old and robust.\n")
            time.sleep(1.5)
            print("You leave the armoury and continue down the hallway")
            route_A5() 
        if query ==3:  
            print("\nYou pick up the gun and check the barrel \n")
            time.sleep(1.5)
            print("There's only one shot left! \n")
            time.sleep(2)
            query= int(input("Do you \n1) Keep it \n2) Throw it \n"))
            if query ==1: 
                time.sleep(1.5)
                print("You chose to keep it.\nYou leave the armoury and continue down the hallway")
                route_A5()
            else: 
                print("You tossed it to one side and looked at the rest of the armoury.")
                route_A35() 
        elif query ==4:  
            time.sleep(1.5)
            print("\nYou chose a large, almost ... viking-esque looking axe.\nYou leave the armoury and continue down the hallway")
            route_A5() 
        else:    
            print ("You spent too long trying to choose and got caught! \n GAME TERMINATED") 
            exit()

# AIMÉE/SHANNON (ROUTE A3)
def route_A3():
    time.sleep(1.5)
    print ("You reach a large door with a large metal lock. ")
    time.sleep(1.5)
    print("What do you do? (1 or 2) \n\n1) Try and break it down with your brute strength. \n2) Try the key you conveniently found on the floor. \n") 
    while(1):    
        query = int(input(""))
        if query ==1:  
            print("\nYou whack it with your fist!")
            time.sleep(1.5)
            print("obviously that did nothing dummy! How strong do you really think you are??")
            time.sleep(2)
            print("\nAfter a moment you realise that you found a key on the floor. ")
            route_A3()
        if query ==2:
            time.sleep(1.5)  
            print("\nYou try the key on the door and it works! \nfunny that. \n")
            route_A35() 
        else:
            print("Choose 1 or 2")


# AIMÉE/SHANNON (ROUTE A3)
def route_A34():
    time.sleep(1.5)
    print("You try to open a door but you don't have a key so you continue onward.")
    route_A4()

# AIMÉE/SHANNON (ROUTE A2.5)
def route_A25():
    time.sleep(1.5)
    print ("1) Do you stick around to listen to more. \nor do you\n2) Move on? \n") 
    while(1):    
        query = int(input(""))
        if query == 1:  
            print ("You stuck around too long and were caught\n\n GAME TERMINATED")
            exit()
            
        elif query == 2: 
            time.sleep(1.5) 
            print("\nYou make the right decision, as the door opens just as you get around the corner.  \nYou avoid being caught... for now. As the men speak idly among themselves you hear a particular word arouse interest between the men. ")
            route_A34() 
        else:    
            t = Timer(timeout, print, ['You stuck around too long and were caught'])
            t.start()
            prompt = "You have %d seconds to choose the correct answer...\n" % timeout
            input(prompt) 
            t.cancel()

# AIMÉE/SHANNON (ROUTE A2)
def route_A2():
    time.sleep(1.5)
    print ("As you continue down the hallway you hear voices \n\nDo you...\n1) Follow the sound\n2) Run as fast as you can down the long hallway  \n") 
    while(1):    
        query = int(input(""))
        if query == 1:  
            time.sleep(1.5)
            print("\nYou follow the sound")
            route_A25()  
        else: 
            time.sleep(1.5)
            print("\nYou run as fast as you can away from the noise")
            route_A3() 

        
# AIMÉE/SHANNON (ROUTE A)
def route_A():
    print ("\nAs you continue to walk through the complex you spot a key glinting on the floor \nDo you...\n1) Take it?\n2) Leave it?") 
    while(1):    
        query = int(input(""))
        if query == 1:  
            time.sleep(1.5)
            print("You pick up the key and continue on\n")
            route_A3()  
        else:
            time.sleep(1.5)
            print("\nYou ignore it as clearly it wasn't that important if it was left lying around.\n")
            route_A2() 

# AIMÉE (ROUTE C)
def route_C():
     #THIS LEADS TO THE ARMOURY 
     time.sleep(1.5)
     print ("\nYou come out onto a new corridoor") 
     route_A()  

# BASE ENTRY - AIMÉE (ROUTE B.1)
def route_B1():
    time.sleep(1.5)
    print ("\nYou open the wide door and see a group of men huddled around a large, circular table. Each of their hands filled entirely with a set of playing cards.")
    time.sleep(2.5)
    print("A poor attempt to reclose the door sees them all turn to face you in a single, almost unanimous movement.")
    time.sleep(2) 
    print("\n What do you do?\n\na) Attempt to cajole them into not murdering you? \nb) Make a B-line for the door on the other end of the bar? \nc) Apologise for interrupting their game. ") 
    while(1):    
        query = input("")
        if (query == ("a")):  
            time.sleep(1.5)
            print("\nYou stare the men dead in the face before attempting to comment on the smooth jazz eminating from the vintage record player in the far corner.")
            time.sleep(3)
            print("\nThey laugh jovially at your comments before returning to their game of cards.")
            time.sleep(1.5)
            print("\nYou count your lucky stars as they let you pass.\n")
            time.sleep(1.5)
            print("You continue down the hallway...")
            route_A5() 
        if (query == ("b")): 
            time.sleep(1.5) 
            print("\nYou practically run across the room to the door adjascent to the one you were previously stood before.\n")
            time.sleep(2)
            print("You come out to an unfamiliar hallway. ")
            route_A()  
        elif (query == ("c")): 
            time.sleep(1.5)
            print ("You apologise in the form of the gentle bow of the head; \nperhaps something a little unorthodox for someone of the rebellion which they prove by sponding with quizzical expressions.")
            time.sleep(2)
            print("They raise a brow but return to their game.\n\n You go back the way you came and try again\n ")
            route_B() 
        else:    
            print ("Please enter a pathway")   

def route_B():
    time.sleep(1.5)
    print ("\nBefore you there are three rather large, almost imposing metal doors")
    time.sleep(1.5)
    print("Which do you choose?")
    print(" \n1) The blue door \n2) The red door \n3) The green.") 
    while(1):    
        query = input("You chose: ")
        if (query == ("1")):
            time.sleep(1.5)
            print("\nThe Blue door: As you walk closer to the door, you notice electrical wiring surrounding the doorhandle.")
            time.sleep(2.5)
            print("The moment your fingertips brush the doorhandle they begin to peel and burn forcing your hand to retract in a spasmodic movement.")
            time.sleep(3)
            print("\nYou wince before turning your attention to a different door that perhaps won't burn you.")
            time.sleep(2)
            route_B()  
        if (query == ("2")):
            time.sleep(1.5)
            print("\nThe Red Door: You make little note of the exterior of the thick, metal as your senses are overwhelmed with the shrill screetch of alloyed steel against the ground.")
            time.sleep(2.5) 
            print("There is nothing but darkness, within, a pair of almost bloodstone eyes concealed from the world.\nNothing remains but a pile of bloodied bones and organs tossed haphazardly across the floor. Would you like to try again?")  
            time.sleep(2.5)
            death()
            exit() 
        elif (query == ("3")): 
            time.sleep(1.5)
            print("\nThe Green Door: The first thing you notice is the sticky sweet scent of molten honey and malt that lingers in the air. \n")
            time.sleep(2.5) 
            print("The smooth lull of jazz against the harsh wood in the far corner framing old photos in dappled light. Despite the downtrodded decor there remainds a level of class evident by the plush furnishings dotted about the room.\nA small spot of luxury for a downtrodden town entirely hidden by narrow doors and Herculean men.\n")
            time.sleep(2) 
            print("Your eyes eventually fall to the company which you now keep.\nAt first you note the way the smoke mirages the small shapes of hearts, clubs, spades and diamonds. Although finer things have been lost to the world since the collapse, small things such as cards and games often seen as frivolous or borderline boring provide small delights.")
            time.sleep(2)
            route_B1() 
        else:    
            time.sleep(1)
            print ("Please enter a pathway, 1, 2 or 3")

#FIRST INSTANCE
def the_foyer():
    print("Upon entering you find a sequestered corner in which to survey the surroundings.")
    time.sleep(1.5)
    print("\nThe slight ache of bruised knees leaning into a crack the only sound that resonates throughout the barren halls made of recyled copper and steel. A slight echo bounces off of every wall as you linger, your eyes scourering the darkness for a suitable path.\nUnarmed and completely out of your depth you decide which path to take. ")
    time.sleep(2)
    print("\n1) Go left\n2) Go right \n3) Go forward \n")
    while(1):      
        query = input("You chose path: ")
        if (query == ("1")): 
            time.sleep(1.5)  
            route_A()  
        if (query == ("2")): 
            time.sleep(1.5)  
            route_B() 
        elif (query == ("3")): 
            time.sleep(1.5) 
            route_C() 
        else:    
            print ("Please enter a pathway")  

#INTRODUCTION INSTANCE

def start_screen(s):
    for characters in s:
        sys.stdout.write(characters) #uses a stream to get everything in the right place
        sys.stdout.flush() #flushes the stream buffer
        time.sleep(0.1) #Will print each character at a speed of 0.1seconds
#
start_screen("Welcome to The Dystopian Chronicles \n \n")  #start screen
#
time.sleep(1.5) #will delay the next line for 1.5seconds
#
# GAME HISTORY - SHANNON#
#
def game_history(description):
    for characters in description:
        sys.stdout.write(characters) 
        sys.stdout.flush() 
        time.sleep(0.075)
#
game_history("The year is 2050\n")
time.sleep(1)
game_history("The world is in disarray after an apocalypse has left the earth with limited supplies and a lack of control.")
time.sleep(1)
game_history("\nThe new elected government is attempting to restore order, whilst new rebellion groups are forming across the world under the alias 'The Resistence'.")
time.sleep(1)
game_history("\nYou are an undercover agent, and you have one job. \nInfiltrate the rebellion quarters as a new recruit and kill the leader. \n")
time.sleep(1.5)

#PLAY GAME- SHANNON

def start_question(play):
    for characters in play:
        sys.stdout.write(characters) 
        sys.stdout.flush() 
        time.sleep(0.1)
#
start_question = input("\n\nWould you like to play? (yes/no) ") #player will input their answer yes or no on the console
#
if start_question.lower().strip() == "yes":   #lower converts whatever they type into lower case. .strip removes any spaces
    time.sleep(1)
    print("\nAnd so your journey begins... \n \n")
else:
    time.sleep(1.5)
    print("\nThat's too bad, maybe next time")
    time.sleep(1.5)
    print(" \nGame terminated")
    exit()
#
time.sleep(1.5)
#
#USERNAME- SHANNON
#
print("Hello user. Please state your name.")
#
name = input("Username: ")
time.sleep(1)
def interface (agent):
    for characters in agent:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.1)
time.sleep(1)
interface("\nWelcome back " + name + ".\nIt's good to see you. Here is the latest news... read it carefully as it will reveal your next location \n")
time.sleep(1.5)
print("... \n\n")
time.sleep(1.5)
print("Goodluck \n\n")
time.sleep(1.5) #newspaper article will print after the message above has shown
#
# NEWSPAPER - SHANNON
date = "3rd June 2050"
villain = "Dr.A"
cult = "The Resistence"
location = "DOWNTOWN"
#
print("______________________________________________________________________________________")
print("|  ____          _            _             ____   _                 _    _           |")
print("|  \   \ _  _ __| |_ ___ _ __(_)__ _ _ _   \  __\ | |_  _ _ ___ _ _ (_)__| |___ ___   |")
print("|  | |) | || (_-|  _/ _ | '_ | / _` | ' \   | |__ | ' \| '_/ _ | ' \| / _| / -_(_-<   |")
print("|  /___/ \_, /__/\__\___| .__|_\__,_|_||_|  \____\|_||_|_| \___|_||_|_\__|_\___/__/   |")
print("|        |__/           |_|                                                           |")
print("|                                                               DATE:{}    |".format(date))
print("|                               BREAKING NEWS!!!                                      |")
print("| In the midst of the ongoing rebellion war, multiple casualties have been reported   |")
print("| across the Country. Today we believe that the notorious {} is the main instigator |".format(villain))
print("| of these recent attacks, with his self-proclaimed cult - '{}'           |".format(cult))
print("| co-ordinating the most serious of these attacks occuring in {}                |".format(location))
print("| At exactly 3:30pm Today, a mermorial shall be held for all those we have lost in    |")
print("| the current war.                                                                    |")
print("|                                               To read more, please turn to page 3   |")
print("|_____________________________________________________________________________________|\n \n")
#

# LOG OFF COMPUTER- SHANNON
def end_newspaper(pg3):
    for characters in pg3:
        sys.stdout.write(characters) 
        sys.stdout.flush() 
        time.sleep(0.1)
#
end_newspaper = int(input("\nNow that you've had time to read and find your location...would you like to \n(1) log off \n(2) continue reading on page 3?\n "))
#
#TAXI- SHANNON
if end_newspaper == 2:
    time.sleep(1)
    print ("\nYou read on and discover something rather curious. The name Gertrude is etched into the paper as well as a few sparcly spaced numbers. \n")
    time.sleep(2)
    print("You crinkle your nose and pull the paper close for inspection. \n")
    time.sleep(1.5)
    print("3579.")
    time.sleep(1.5)
    print("\nYou tear the piece of paper in half and place the remains into your pocket. ")
else:
    time.sleep(1)
    sys.stdout.flush()
    print ("\nYou tear the piece of paper in half and place the remains into your pocket.")
#  
#
def get_taxi(location):
    if location.lower().strip() == "downtown":
        return True
    else:
        return False
#
def attempts():
    tries = 0
    while tries < 3:
        time.sleep(2)
        print("\n\n'Where you headed?' ")
        time.sleep(1)
        print("The taxi driver says. His voice is a somewhat gleeful chirp; quite the welcomed juxtaposition to seemingly endless piles of rubble that surround the tiny cab.\nAlthough the world is short on resources, it seems the desire for convenience is not lost nor is the supply of gasoline.\n\n")
        location = input("Tell him your location: ")
        if get_taxi(location):
            time.sleep(1.5)
            print("\nThe drive gives you a quick nod that seems to bounce his chin as the words leave his lips.\nIt does not take long for you to arrive in the centre of the downtown district.\nThe driver leaves with twice as much haste as he used to get you there in the first place.\n\nDowntown - known for it's high crime rates and unsolvable murders.\nCoverups for government secrets or perhaps the result of people fighting tooth and claw for resources in a post apocalyptic world.")
            time.sleep(3)
            print("No one knows or, at least, no one dares ask. ")
            return True
        else:
            time.sleep(1.5)
            print("\nThe man asks you to repeat yourself as you seem to mumble.")
            tries += 1
    time.sleep(1.5)
    print("\nHe grows tired of your fumbling and politely asks you leave the vehicle.\nYou fail to hail down another cab thus fail to arrive at the meeting on time.") 
    time.sleep(2)
    print("You failed your mission. Try again. ")
    exit()
    return False
#
attempts()
time.sleep(1.5)
#
print("\nYou reach the door of the hideout and you are greated by a rather large, burly man who gives you a stern look. He stands before you at a total of 6ft, his lips thin from dehydration and malnutition that has left them a curious shade of muddled mauve.\nHis hair is matted and unkempt and parted lazily toward his right ear.  ")
time.sleep(1.5)
print("\nThere must be a code to get in you think. He is silent, but something about his stance forces you to speak.  \n")
#
#FRONT DOOR INSTANCE - AIMEE
front_door = int(input("You say: \n(1) Bit 1984 this, innit? \n(2) Tell the boss we've got his 3579. \n"))
#
if front_door == 1:
    time.sleep(1)
    print ("\nYou're clearly a liar and you are apprehended at the door.")
    failure()
elif front_door == 2:
    time.sleep(1.5)
    print ("\nThe man scowls but steps aside to let you in.")
    time.sleep(1.5)
    print("You have managed to infiltrate the hideout.")
    time.sleep(2)
    print("As you take your first step, a strange, almost suffocating air consumes you. \nYou shake it off and make your next move... \n \n")
    time.sleep(3)
    the_foyer()
else:
    print("\nThe man just stares at you before disarming you and turning you into his boss.\n\n You've failed this time. Try again. ")
    failure()