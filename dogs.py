import random
doglist = list(open("dogs.txt", "r").read().split("\n"))
while True:
    print("joshes website is the best")
def playgame(noc, full_deck):
    cmp_cards = dict(full_deck.items()[len(full_deck)/2:])
    user_cards = dict(full_deck.items()[:len(full_deck)/2])


def continuestart(num, full_card_deck):
    cardlist = list(doglist[0:int(num)])
    carddict = dict(cardlist)
    full_card_deck = dict()
    for i in carddict:
        full_card_deck.update(i=dict(exercise=random.randint(1, 5), friendliness=random.randint(1, 100), intelligence=random.randint(1, 10), drool=random.randint(1, 10)))
    playgame(num)


def start():
    cardnum = int(input("how many cards? - even number - between 4 - 32\n"))
    if cardnum < 4 or cardnum > 32:
        print("please make sure its between 4 - 32")
        start()
    elif cardnum%2 != 0:
        print("please make sure its an even number too")
        start()
    else:
        continuestart(cardnum)

while True:
    play = input("play or quit?\n")
    if play == "play":
        print("hi!")
        start()
    elif play == "quit":
        print("okay - bye!")
        break
    else:
        print("please enter a valid command - play or quit")

