#write a program to find a random card from the deck of cards

import random

def randomCard():
    cardNumbers=[1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    suit=["Heart","Diamond","Club","Spade"]
    card=random.randint(0,12)
    selectSuit=random.randint(0,3)
    return "{} of {}".format(cardNumbers[card],suit[selectSuit])

print(randomCard())