# ------------------------------------------------------
#        Name: #Susannah Winfield
#       Peers: (add any collaborators)
#  References: https://www.geeksforgeeks.org/python/python-extract-words-from-given-string/
# ------------------------------------------------------
import sys

secret_word = "test"
secret_dogs = ["dog","Dog"]
# Task 1

def check_text():
    """ checks user input for secret words
asks for a sentence, checks if dog, Dog, or value stored in secret_word is in that input.
If input contains Dog or dog it prints 'You used the word "dog" or the word "Dog"!' and stops
If input contains secret_word, it prints "You used the secret word!" and stops
If the input does not have dog, Dogs or secret_word, it prints 'Try Again' and repeats the loop.

Returns nothing
"""
def check_text():
    cap_secret_word = secret_word.capitalize()
    secret_list = [secret_word, cap_secret_word]
    sentence = input("Give me a sentence: ")
    while True:
        if any(word in sentence for word in secret_list):
            print("You used the secret word!")
            return
        if any(dog in sentence for dog in secret_dogs):
            print('You used the word "dog" or the word "Dog"!')
            return

        print("Try again")
        sentence = input("Give me a sentence: ")

    #print(f'You used the word "{secret_word}" or the word "{cap_secret_word}"')




# Task 2
def check_greater():
    """Test input numbers
Asks for two integers:
    > repeats the loop when they are equal
    > Prints 'First is Greater' is the first input integer is greater
    > Prints 'Second is Greater' is the second input integer is greater

returns nothing
"""
    first = int(input("give me a first integer: "))
    second = int(input("give me a second integer: "))
    while first == second:
        print("Try again")
        first = int(input("give me a first integer: "))
        second = int(input("give me a second integer: "))
    if first > second :
        print("First is Greater")
    else :
        print("Second is Greater")




# Task 3
def get_special_numbers():
    """ Prints certain numbers
checks each number from 1 to 40 and prints only those that are divisible by 3, odd, and not divisible by 5

"""
    for num in range(1,40):
        if num%3 == 0 and num%5 != 0 and num%2 != 0:
            print(num)



# Task 4.a
def my_for_loop():
    """ Identifies letters
takes an word input 
checks that that input is between 2 and 5 letters and does not have any spaces, if it isn't valid the function returns.
prints the letter and says if it is a vowel or a consonant

for example if 'and' is inputted it will print:

valid
a is a vowel
n is a consonant
d is a consonant

if an invalid string like 'a string' is input it will print:

Give a word between 2 and 5 letters: a string
bad word

Returns nothing
"""
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    UserWord = str(input("Give a word between 2 and 5 letters: "))
    if len(UserWord) in range(2,5) and " " not in list(UserWord):
        print("valid")
    else:
        print("bad word")
        return
    for letter in UserWord:
        if letter in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")
            
# Task 4.b
def my_while_loop():
    """ Add your docstring """
    choice = input("Give me a,b, or c: ")
    while choice == "a":
        choice = input("Give me a,b, or c: ")
    if choice == "b":
        print("Goodbye")
        return
    if choice == "c":
        exit()

    while choice not in ["a", "b", "c"]:
        if choice == "c":
            exit()
        print("try again")
        choice = input("Give me a,b, or c: ")
        if choice == "b":
            print("Goodbye")
            return
       
        while choice == "a":
            choice = input("Give me a,b, or c: ")
    
        


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
