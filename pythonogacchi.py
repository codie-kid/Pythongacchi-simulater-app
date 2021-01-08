#Define the creature Class

import random 
class Creature():
    def __init__(self, name):
        """Initialize attributes"""
        self.name = name.title()


        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtness = 0

        self.food = 2 #represent food inventry
        self.is_sleeping = False #Bool to track if the creature is sleeping
        self.is_alive = True #Bool to track if the creature is alive


    def eat(self):
        """Simulate Eating  .Each time you eat take one food away from the inventory"""
        if self.food>0:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print("Yum! " + self.name + "ate a great meal")
        else:
            print(self.name + "doesn't have any food! Better forage for some")
        
        if self.hunger < 0:
            self.hunger = 0


    def play(self):
        """Play a guessing game to lower the creatures boredom"""
        value = random.randint(0,2)
        print("\n" + self.name + " wants to play a game")
        print(self.name + "is thinking of a number 0 ,1 or 2")
        guess = int(input("what is your guess: "))

        #lower the boredom attribute based on the user
        if guess == value:
            print("That is correct!!!")
            self.boredom -=3
        else:
            print("WRONG!!" + self.name + "was thinking of " + str(value) + ".")
        

        if self.boredom < 0:
            self.boredom = 0
    def sleep(self):
        self.is_sleeping = True
        self.tiredness -=3
        self.boredom -=2
        print("Zzzzzz.......zzzzzzz.........zzzzzzz.......")

        #if tiredness or boredom is less than 0 set it to 0
        if self.tiredness <0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        """Simulate randomly waking a creature up"""
        value = random.randint(0,2)
        if value == 0:
            print(self.name + "just woke up!")
            self.is_sleeping = False
            self.tiredness = 0
        else:
            print(self.name + "won't wake up")
            self.sleep()

    def clean(self):
        """Simulate taking a bath to completly clean creature"""
        self.dirtness = 0
        print(self.name + "has taken a bath. All clean!")


    def forage(self):
        """Simulate foraging for food"""
        food_found = random.randint(0,4)
        self.food += food_found

        #creature get dirty from foraging
        self.dirtness +=2

        print(self.name + "found" + str(food_found)+ "piece of food!")

    
    def show_values(self):
        """Show the current information about creature"""
        print("\n Creature Name: " + self.name)
        print("Hunger (0-10) : " + str(self.hunger))
        print("Boredom (0-10) : " + str(self.boredom))
        print("Tiredness (0-10) : " + str(self.tiredness))
        print("Dirtness (0-10) : " + str(self.dirtness))

        print("\nFood Inventory : " + str(self.food) + " pieces")
        if self.is_sleeping:
            print("Current Status : Sleeping")
        else:
            print("Current Status : Awake")
        
    
    def incriment_value(self , diff):
        self.hunger += random.randint(0,diff)
        self.dirtness += random.randint(0,diff)

        if self.is_sleeping == False:
            self.boredom += random.randint(0,diff)
            self.tiredness += random.randint(0 , diff)



    def kill(self):
        """"check  for all conditions to kill or sleep the creature."""
        if self.hunger >= 10:
            print(self.name + "has starved to death...")
            self.is_alive = False
        elif self.dirtness>= 10:
            print(self.name + "has suffered an infection and died...")
            self.is_alive = False
        elif self.boredom >=10:
            self.boredom = 10
            print(self.name + "is bored , Falling asSleep...")
        elif self.tiredness >=10:
            self.tiredness = 10
            print(self.name + "is sleepy. Falling asleep..")
            self.is_sleeping = True

#Helper function outside of the creature class
def show_menu(creature):
    if creature.is_sleeping:
        choice = int(input("Enter (6) to try and wake up"))
        choice  = '6'
    else:
        print("\n Enter 1 to eat")
        print("Enter 2 to play")
        print("Enter 3 to sleep")
        print("Enter 4 to take bath")
        print("Enter 5 to forage for food")
        choice = input("What is your choice")
    return choice

def call_action(creature , choice):
    """given the player choice , call the appropriate class method"""
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.awake()
    else:
        print("Sorry, that is not a valid move")

#The main code
print("Welcome to the pytthonagachi Simulater App")

difficulty = int(input("Please choose a difficulty level (1-5)"))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty =1

#The overall main game loop
running = True
while running:
    name = input("What name would you like to give your pet Pythonagachi")
    player = Creature(name)

    round = 1
    #The loop should run as long as creature is alive
    while player.is_alive:
        print("\n----------------------------------------------------------")
        print("Round#" + str(round))
        #An individual round should show the values, and get a player mpove
        player.show_values()
        round_move = show_menu(player)
        call_action(player,round_move)

        print("Round #" + str(round) + "Summary: ")

        player.show_values()
        input("\nPress (enter) to continue...")

        #Increment values and check for death
        player.incriment_value(difficulty)
        player.kill()

        #Round is over

        round += 1
    #The creature has died. Game over
    print("\nR.I.P")
    print(player.name + "survived total of " + str(round - 1) + "rounds.")

    #Ask the user to play it again
    choice = input("Would you like to play again (y/n) : " ).lower()
    if choice!= 'y':
        running = False
        print("Thank you for playing Pythonagachi ")






    
