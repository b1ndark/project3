# import random, so cards can be shuffled in the game
import random
# import os to clear terminal
import os

# Variable
USERNAME = ""


# Function to clear screen
def clean():
    os.system("clear")


# Function to show instructions
def instructions():
    clean()
    print("*" * 40)
    print(f"\n {USERNAME} welcome to the instructions! \n")
    print("*" * 40)
    print("*" * 40)
    print("\n  Main goal is to either get 21 points\n\
    or to be as close as possible\n\
        \n  If you go above 21 you automatically\n\
             lose the game\n")
    print("    The dealer will ask you whether\n\
        you want to Hit or Stay\n")
    print("   2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6\n\
  7 = 7, 8 = 8, 9 = 9, J = 10, Q = 10\n\
    K = 10, and finally A = 1 or 11\n")
    print("  The main goal is to beat the dealer!\n")
    print("*" * 40)

    print("\nPlease select from the following options:")
    # While loop to loop through the try/except and if statements
    while True:
        numberEntered = input("\n   1: Start.\n   2: Exit.\n")
        # Try/Except to check whether is a number or not
        try:
            numberEntered = int(numberEntered)
        except:
            print("\n      ****Invalid Input Entered****")
        # If statement to check what option user has selected
        # Loop will break once option is selected
        if numberEntered == 1:
            start()
            break
        elif numberEntered == 2:
            mainMenu()
            break
        else:
            print("Please select a number from the options:")


class cardSelected:
    # init function to create an object in this case, to create a card
    def __init__(self, cardSuit, cardRank):
        self.cardSuit = cardSuit
        self.cardRank = cardRank

    # to create and return a readable string of the card
    def __str__(self):
        return f"{self.cardRank['rank']} of {self.cardSuit}"


class cardsDeck:
    def __init__(self):
        self.cards = []
        # List of card suits
        cardSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        # Dictionary list with card ranks and their respective values
        cardRanks = [
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
            {"rank": "A", "value": 11},
        ]

        # Append cardSuits and cardRanks onto cards list 'cards = []'
        for cardSuit in cardSuits:
            for cardRank in cardRanks:
                self.cards.append(cardSelected(cardSuit, cardRank))

    # To shuffle the cards list
    def shuffleCards(self):
        # When shuffling cards it will check if theres more than one left
        if len(self.cards) == 1:
            pass
        else:
            random.shuffle(self.cards)

    # Function to deal cards, once they are dealt they also will be popped
    # And moved to cardsDealt
    def dealCard(self, number):
        cardsDealt = []
        for i in range(number):
            # To check whether there are any cards left to be removed
            if len(self.cards) == 0:
                pass
            else:
                card = self.cards.pop()
                cardsDealt.append(card)
        return cardsDealt


class handCard:
    def __init__(self):
        self.cards = []
        self.value = 0

    # Extend method to add each card to cardList
    def addCard(self, cardList):
        self.cards.extend(cardList)

    def cardValueCalculate(self):
        self.value = 0
        self.ace = False

        for card in self.cards:
            cardValueCalculate = int(card.cardRank["value"])
            self.value += cardValueCalculate

    # To calculate the value of the cards
    def displayValue(self):
        self.cardValueCalculate()
        return self.value

    # Function to display the cards and their total value
    def display(self):
        print(f'{USERNAME} your cards are:')

        for card in self.cards:
            print(card)
        print("Total value of:", self.displayValue())
            
        print()


   

deck1 = cardsDeck()
deck1.shuffleCards()

handCard = handCard()
handCard.addCard(deck1.dealCard(5))
#handCard.display()


# Main Menu function where you will be able to select Instructions
# Or start the game
def mainMenu():
    clean()
    print("*" * 40)
    print(f"\n   {USERNAME} welcome to BlackJack Game \n")
    print("*" * 40)
    print("*" * 40)
    print("\nPlease select from the following options:")

    # While loop to loop through the try/except and if statements
    while True:
        numberEntered = input("\n   1: Instructions.\n   2: Start.\n")
        # Try/Except to check whether is a number or not
        try:
            numberEntered = int(numberEntered)
        except:
            print("\n      ****Invalid Input Entered****")
        # If statement to check what option user has selected
        # Loop will break once option is selected
        if numberEntered == 1:
            instructions()
            break
        elif numberEntered == 2:
            handCard.display()
            break
        else:
            print("Please select a number from the options:")


# This function will ask the user to type the username
def userName():
    clean()
    print("*" * 40)
    print("\n        Welcome to BlackJack Game \n")
    print("*" * 40)
    print("*" * 40)

    # While loop to loop through the try/except and if statements
    # To check whether username has been entered or not
    while True:
        global USERNAME
        USERNAME = input("\nPlease enter your username:\n")
        # Check for spaces
        if USERNAME.isspace() is True:
            print("Please enter username in order to proceed")
        # Check for blank input
        elif USERNAME == "":
            print("Please enter username in order to proceed")
        # Check if user entered symbols or numbers
        elif USERNAME.isalpha() is False:
            print("Only letters accepted")
        else:
            mainMenu()


userName()
