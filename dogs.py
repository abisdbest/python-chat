doglist = list(open("dogs.txt", "r").read().split("\n"))

def continuestart():
    print("ok")


def start():
    cardnum = int(input("how many cards? - even number - between 4 - 32\n"))
    if cardnum < 4 or cardnum > 32:
        print("please make sure its between 4 - 32")
        start()
    elif cardnum != 0%2:
        print("please make sure its an even number too")
        start()
    else:
        continuestart()

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

