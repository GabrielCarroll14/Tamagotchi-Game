# Import the random module  
import random

# Create the variables for the health stats of the tamagotchi
happiness = 100
energy = 100
cleanliness = 100

# Create a random variable for the keytrait of the tamagotchi
keytrait = random.choice (["angry", "cute", "stupid", "pathetic", "kind", "queasy", "clever", "loyal", "freaky", "hyper", "cheeky",])

# Create the cat tamagotchi image variable
cat = '''
 /\_/\ 
( o.o )
 > ^ <
'''
# Create the rabbit tamagotchi image variable
rabbit = '''
 (\\(\\ 
 ( -.-) 
 o_(")(")
'''
# Create the dog tamagotchi image varible
dog = '''
 / \\__
(    @\\____
 /         O
/   (_____/
/_____/   U
'''

# Ask the user what they want to name the tamagotchi
name = input ("What do you want your tamagotchi to be called? ")

# Give user a message relaying the name they just input for the tamagotchi
print ("You have chosen to name your tamagotchi " + name + "! ")

# Ask the user what animal they want the tamagochi to be
print ("What animal would you like your tamagotchi to be? ")

# Give a list of the different options for types of animals for the user to choose
print ("1. Rabbit ")
print ("2. Cat ")
print ("3. Dog ")

# Now ask the question of which one they would like to choose
answer = int(input("Which would you like to choose? "))

# Match up the answers for the animals they could choose

# Match up with rabbit
if answer == 1:
    print ("You have selected Rabbit! ")
    animal = rabbit
    print (animal)
    type = "Rabbit"
# Match up with cat
elif answer == 2:
    print ("You have selected Cat! ")
    animal = cat
    print (animal)
    type = "Cat"
# Match up with dog  
elif answer == 3:
    print ("You have selected Dog! ")
    animal = dog
    print (animal)
    type = "Dog"

# Print a message from the tamagotchi displaying the name, keytrait and type.
print ("Hello, my name is " + name + ". I am a " + keytrait + " " + type + "! ")

# Display a few more messages to the user
print ("Your job is to look after me! ")
print ("You will have a dashboard of how I am feeling! ")


# Show user dashboard menu

# Create the loop
for number in range(300000000):
    
    # Tamagotchi will die if happieness gets to low
    if happiness < 1:
        print ("Your " + type + " is dead, because it got to sad")
        break
    
    # Tamagotchi will die if energy gets to low
    if energy < 1:
        print ("Your " + type + " is dead because it got to tired!")
        break
    
    # Tamagotchi will die if cleanliness gets to low
    if cleanliness < 1:
        print ("Your " + type + " is dead because it got to dirty!")
        break
    
    # Print the image of the animal
    print (animal)
    
    # Print the different heath stats of the animal
    print ("1. My happiness is " + str(happiness) + "% ")
    print ("2. My energy is " + str(energy) + "% ")
    print ("3. My cleanliness is " + str(cleanliness) + "% ")
    
    # Ask user for a dashboard setting. 1,2,3
    dash = int(input("Which would you like to choose? "))
    
    # Make it so if the users input is equal to 1 it will bring the user to the happiness menu
    if dash == 1:
        print (" ")
        
        # Print a message to the user confirming that they chose the happiness menu
        print ("You have selected the happiness menu! ")
        print ("1. Take for walk. ")
        print ("2. Stroke. ")
        print ("3. Feed. ")
        hapmenu = int(input("Select a option. "))
        
        # Option 1 where user has chosen to take animal for a walk
        if hapmenu == 1:
            print ("You have taken your " + type + " for a walk")
            ran = random.randint (1,3)
            # Option when the walk went good
            if ran == 1:
                happiness = happiness + 10
                print ("Your walk went sucsessfully and now your " + type +" has a extra 10% happiness!")
            # Option when the walk went good
            if ran == 2:
                happiness = happiness + 10
                print ("Your walk went sucsessfully and now your " + type + " has a extra 10% happiness!")
            # Option when the walk went bad
            if ran == 3:
                happiness = happiness - 40
                print (" ")
                print ("On your walk your " + type + " ate a stick, the vet was able to sort it out but it still really hurts! -40 happiness! ")
            
        # Option where the user decides to stroke the animal
        elif hapmenu == 2:
            print ("You have chosen to stroke your " + type + ". ")
            ran = random.randint (1,3)
            # Option when the stroking went good
            if ran == 1:
                happiness = happiness + 10
                print ("")
                print ("You stroked your " + type + " sucsessfully! extra 10% happiness!")
            # Option when the stroking went good
            if ran == 2:
                happiness = happiness + 10
                print (" ")
                print ("You stroked your " + type + " sucsessfully! extra 10% happiness!")
            # Option when the stroking went bad
            if ran == 3:
                happiness = happiness - 40
                print (" ")
                print ("When you were stroking your " + type + " you got a ergent phone call and had to leave your " + type + ". he now thinks you dont love him! -40 happiness! ")
                
        # Option where the user decides to feed the animal
        elif hapmenu == 3:
            print ("You have chosen to feed your " + type + ". ")
            ran = random.randint (1,3)
            # Option when feeding went good
            if ran == 1:
                happiness = happiness + 10
                print (" ")
                print ("You fed your " + type + " sucsessfully! extra 10% happiness!")
            # Option when feeding went good
            if ran == 2:
                happiness = happiness + 10
                print (" ")
                print ("You fed your " + type + " sucsessfully! extra 10% happiness!")
            # Option when the feeding went bad
            if ran == 3:
                happiness = happiness - 40
                print (" ")
                print ("When you were feeding your " + type + ", they began to choke, you managed to do the hiemlich menouver, but your " + type + " is still traumatised.  -40 happiness! ")
        else:
            pass
            
    # Energy menu
    elif dash == 2:
        print (" ")
        print ("You have selected the energy menu! ")
        print ("1. Give sweets! ")
        print ("2. Take to animal gym. ")
        print ("3. Feed. ")
        engmenu = int(input("Select a option. "))
        
        # OPtion where user decides to give animal sweets
        if engmenu == 1:
            print ("You have decided to give sweets to your " + type + ". ")
            print ("Your " + type + " fell very unwell because of the sweets you gave. -50 Everything!" )
            happiness = happiness - 50
            energy = energy - 50
            cleanliness = cleanliness - 50
            
        # Option where the user decides to take animal to gym
        elif engmenu == 2:
            print ("You have chosen to take your " + type + " to the gym with you. ")
            ran = random.randint (1,3)
            # Option when going to the gym went good
            if ran == 1:
                energy = energy + 10
                print (" ")
                print ("When you took your " + type + " to the gym, they gained extra muscle and are now full of energy! + 10 Energy!")
            # Option when going to the gym went good
            if ran == 2:
                energy = energy + 10
                print (" ")
                print ("When you took your " + type + " to the gym, they gained extra muscle and are now full of energy! + 10 Energy!")
            # Option when going the gym went bab
            if ran == 3:
                energy = energy - 40
                print (" ")
                print ("When you were taking your " + type + " to the gym, one of the weights fell on them.  -40 energy! ")
            else:
                pass
                
        
         # Option where the user decides to feed the animal
        elif engmenu == 3:
            print ("You have chosen to feed your " + type + ". ")
            ran = random.randint (1,3)
            # Option when feeding went good
            if ran == 1:
                energy = energy + 10
                print (" ")
                print ("You fed your " + type + " sucsessfully! extra 10% energy!")
            # Option when feeding went good
            if ran == 2:
                energy = energy + 10
                print (" ")
                print ("You fed your " + type + " sucsessfully! extra 10% energy!")
            # Option when the feeding went bad
            if ran == 3:
                energy = energy - 40
                print (" ")
                print ("When you were feeding your " + type + ", they began to choke, you managed to do the hiemlich menouver, but your " + type + " is still traumatised.  -40 energy! ")
                
    elif dash == 3:
        print (" ")
        print ("You have selected the cleanliness menu! ")
        print ("1. Give wash!")
        print ("2. Comb")
        print ("3. Trim hair. " )
        clemenu = int(input("Select a option. "))
        
        # Option 1 where you give animal a wash
        if clemenu == 1:
            # If animal cat rusult not good
            if type == "Cat":
                print ("Cats dont like water! -30 Happiness but + 10 cleanliness!")
                cleanliness = cleanliness + 10
                happiness = happiness - 30
            else:
                cleanliness = cleanliness + 10
                print ("You sucsessfully cleaned your " + type + "! + 10 cleanliness!")
                
        # Option 2 where you comb your animal
        elif clemenu == 2:
            print ("You have chosen to comb your " + type + ". ")
            ran = random.randint (1,3)
            # Option when combing went good
            if ran == 1:
                cleanliness = cleanliness + 10
                print (" ")
                print ("You combed your " + type + " sucsessfully! extra 10% cleanliness!")
            # Option when combing went good
            if ran == 2:
                cleanliness = cleanliness + 10
                print (" ")
                print ("You combed your " + type + " sucsessfully! extra 10% cleanliness!")
            # Option when the combing went bad
            if ran == 3:
                happiness = happiness -40
                cleanliness = cleanliness - 40
                print (" ")
                print ("When you were combing your " + type + ", there hair got tangled! -40 happiness and cleanliness! ")
        
        # Option 2 where you trim your animal
        elif clemenu == 3:
            print ("You have chosen to trim your " + type + ". ")
            ran = random.randint (1,3)
            # Option when trimming went good
            if ran == 1:
                cleanliness = cleanliness + 10
                print (" ")
                print ("You trimmed your " + type + " sucsessfully! extra 10% cleanliness!")
            # Option when trimming went good
            if ran == 2:
                cleanliness = cleanliness + 10
                print (" ")
                print ("You trimmed your " + type + " sucsessfully! extra 10% cleanliness!")
            # Option when the trimming went bad
            if ran == 3:
                cleanliness = cleanliness - 40
                happiness = happiness - 40
                print (" ")
                print ("When you were trimming " + name + ", you got carried away and they became bald! Now they are always freezing! -40 happiness and cleanliness")
    else:
        print ("This is not a valid input please select a different option. ")  