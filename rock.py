import random
print('WELCOME TO ROCK*PAPER*SCISSORS GAME')
print('YOUR CHOICES ARE- rock/paper/scissors')
li=['rock','paper','scissors']
r=['paper','scissors']
p=['rock','scissors']
s=['rock','paper']
#for i in range(3):
choice=(input("ENTER YOUR CHOICE:"))
#rock
def rock():
    if choice==li[0]:
        g=random.choice(r)
        print("COMPUTER'S CHOICE:",g)
        if g=='scissors':
            print('YOU WON')
        else:
            print('COMPUTER WON')
rock()
#paper
def paper():
    if choice==li[1]:
        g=random.choice(p)
        print("COMPUTER'S CHOICE:",g)
        if g=='rock':
            print('YOU WON')
        else:
            print('COMPUTER WON')
paper()
#scissors
def scissors():
    if choice==li[2]:
        g=random.choice(s)
        print("COMPUTER'S CHOICE:",g)
        if g=='paper':
            print('YOU WON')
        else:
            print('COMPUTER WON')
scissors()
