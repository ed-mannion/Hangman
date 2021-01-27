'''
Project 2:
Hangman

Play a game of Hangman

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
import random
import time

random_words = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]
# This is a nested list for drawing the gallows
gallows = [[" "," ","+","-","-","-","+"," "], [" "," ","|"," "," "," ","|"," "], [" "," "," "," "," "," ","|"," "],[" "," "," "," "," "," ","|"," "],[" "," "," "," "," "," ","|"," "],[" "," "," "," "," "," ","|"," "],["=","=","=","=","=","=","=","="] ]
# This tuple contains the indices of the list elements to be replaced by the included limb
body_part_location = ((2,2,"O"),(3,2,"|"),(3,1,"/"),(3,3,"\\"),(4,1,"/"),(4,3,"\\"))
remaining_guesses = 6
bad_guesses = 0
guessed_word = ""
winner = False
guessed_so_far = []

# Take a word and convert it into a list of blanks equal to it's length and a list of it's characters
def convert_word(word):
    blanks = []
    word_as_list = list(word)
    for i in range(len(word)):
        blanks.append("_")
    return blanks, word_as_list

# Print the gallows in it's current state
def print_gallows(gallows):
    for row in range(7):
        for col in range(8):
            if col !=7:
                print(gallows[row][col], end = "")
            else:
                print(gallows[row][col])

# Add the stickman to the board piece by piece. The coordinates for each piece are in a touple along with the limb.
# This adds a limb for wach bad guess.
def process_incorrect_guess(body_part_location, bad_guesses):
    count = 0
    for row, col, part in body_part_location:
        gallows[row][col] = part
        count += 1
        if bad_guesses == count:
            break

# Check to see if a guess is correct by comparing the guessed letter with the list version of the word.
# If the guess is correct the "-" is replaced by the guessed letter        
def guess_correct(guess):
    indices = [i for i,x in enumerate(hidden_word) if x == guess]
    if len(indices) == 0:
        return False
    else:
        for i in range(len(indices)):
            index = int(indices[i])
            display_word[index] = guess

# Ask player 2 to enter a word, confirm the word and clear the screen.
def get_word_from_player():
    word = input("Player 1, please enter a word: ")
    word = word.upper()
    time.sleep(1)
    print(f"OK, got it, you chose {word}")
    time.sleep(1)
    print(chr(27) + "[2J")
    return word

# Get a random word from the list of words above
def get_word_from_computer():
    random_word = random_words[random.randint(0,99)]
    return random_word

# Start playing the game
game_type = int(input("1 or 2 players?: "))

if game_type == 1:
    word = get_word_from_computer()
    word = word.upper()
    player1 = "Computer"
else:
    word = get_word_from_player()
    player1 = "Player 1"
    
display_word, hidden_word = convert_word(word)

# Continue the game until a win condition is met
while winner == False:
    print(chr(27) + "[2J")
    print_gallows(gallows)
    print("\n")
    print(f"Guesses left: {remaining_guesses}\n")
    print(*display_word)
    guess = input("\nPlayer 2, guess a letter: ")
    guess = guess.upper()
    # If the guess is incorect decrement the number of remaining guesses and increment the bad guess count.
    # Let the player know that the guess was wrong
    if guess in guessed_so_far:
        print(f"You already tried {guess}.")
    elif guess_correct(guess) == False:
        remaining_guesses -= 1
        bad_guesses += 1
        print(f"{guess} is not in the word. You have {remaining_guesses} guesses left.")
        process_incorrect_guess(body_part_location, bad_guesses)
        guessed_so_far.append(guess)
    # If the guess was correct create a new string from the list of correct guesses and "-"s
    # This will be used for a comparison later
    else:
        guessed_word = ''.join(display_word)
        guessed_so_far.append(guess)
        
    time.sleep(1)

    if remaining_guesses == 0:
        # Clear the screen and let the Player 2 know he lost
        print(chr(27) + "[2J")
        print_gallows(gallows)
        print(f"The word was \'{word}\'. \n{player1} Wins")
        winner = True
    elif guessed_word == word:
        print(f"Correct! The word is \'{word}\'. \nPlayer 2 Wins")
        winner = True