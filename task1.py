'''Create a program to compare three numbers and find the bigger numbers. 
[topics covered: identified, variable, types, operator, if statement]'''
'''
a=int(input("enter first number: "))
b=int(input('enter second number: '))
c=int(input('enter third number: '))

if (a>b and a>c):
    print("The First number ",a," is bigger")
elif(b>a and b>c):
    print("The Second number ",b,' is bigger')
else:
    print("The Third number ",c,' is bigger')
    
'''

'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

'''
name=str(input("Enetr the name: "))
age = int(input("Enter age: "))

if(age>=100):
    print('you are 100 years old')


'''

'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissorsScissors beats paperPaper beats rock'''

#Rock vs paper-> paper wins
#Rock vs scissor-> Rock wins
#paper vs scissor-> scissor wins.

'''
a=['Rock','rock','Paper','paper','Scissor','scissor']
x=input('Player 1 -->> enter your choice: ')
if x in a:
    print('correct choice')
else:
    print("incorrect choice")

y=input('Player 2 -->> enter ur choice: ')

if y in a:
    print('correct choice')
else:
    print("incorrect choice")


if (x == y):
    print("tie")
elif (x=='Rock' or 'rock') and (y=='paper' or 'Paper'):
    print('Paper beats Rock')
elif (x=='Rock' or 'rock') and (y=='Scissor' or 'scissor'):
    print('Rock beats Scissor')
elif (x=='Paper' or 'paper') and (y=='Scissor' or 'scissor'):
    print('Scissor beats Paper')


'''

"""
n=int(input("Enter how many numbers u want in list\n"))
a=list()
for i in range(n):
    p=int(input('enter the number: '))
    a.append(p)
print(a)

p=0
repeated=int(input("Which number's repeatation u want to checked: "))

for i in a:
    if i==repeated:
        p=p+1
    else:
        continue
print("The number ",repeated," is repeated ",p,"times")

"""




#Write the above solution in a function which takes take numbers and return the bigger number [topic covered: function]
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
def func(a=0,b=0,c=0):
    if(a>b and a>c):
        print("the bigger value is", a)
    
    elif(b>a and b>c):
        print("the bigger value is ",b)
    else:
        print("the bigger value is ",c)
    return

print(func(a,b,c))
'''

#2
'''
name=str(input("Enetr the name: "))
age = int(input("Enter age: "))

def com(name,age):
    if(age>=100):
        print('you are 100 years old')

print(com(name,age))
'''

#3

#Rock vs paper-> paper wins
#Rock vs scissor-> Rock wins
#paper vs scissor-> scissor wins.

def comp(ch1,ch2):
    if(ch1==ch2):
        print("Tie")
    elif(ch1=='rock'):
        if(ch2=='scissor'):
            print("rock beats scissor")
        else:
            print("paper beats rock")

    elif(ch1=='paper'):
        if(ch2=="rock"):
            print("paper beats rock")
        else:
            print("scissor beats rock")

    elif(ch1=='scissor'):
        if(ch2=="rock"):
            print("rock beats paper")
        else:
            print("scissor beats paper")

def repeat():
    rep=str(input("Do you wanna play again?(Y/N)"))
    if(rep=='n' or 'N'):
        return

ch1=str(input("Player1::Rock, Paper, Scissor? "))
ch2=str(input("Player2::Rock, Paper, Scissor? "))

comp(ch1,ch2)
repeat()