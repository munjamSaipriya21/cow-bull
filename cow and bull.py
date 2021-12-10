import random
def cowbull_numbers(number, user_guess):
    list1 = [1,2,3,4,5,6,7,8,9]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
             list1[1]+=1
        else:
            list1[0]+=1
    return  list1

if __name__=="__main__":
    playing = True 
    number = str(random.randint(0,9999))
    guesses = 0

    print("Let's play a game of Cowbull!") 
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!:")
        if user_guess == "exit":
            break
        cowbullcount = cowbull_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break 
        else:
            print("Your guess isn't quite right, try again.")
            break
cowbull_numbers([2,4],[3,5])


