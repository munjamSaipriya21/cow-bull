import random

a = random.randint(1000,9999)
b=[int(i) for i in str(a)]
guess=0
playing=True
while playing:
    
    c=input('Guess 4 digit number: ')
    d=[int(i) for i in str(c)]
    cow=4
    bull=0
    for i in range(len(c)):
        if b[i] == d[i]:
            bull += 1
            cow -= 1
    guess += 1
    print('You have ',cow,'cows and',bull,'bulls')
    if bull==4:
        print('Correct!!! you guessed',a,'in',guess,'tries')
        break