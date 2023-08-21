##############################################BNF GRAMMAR###########################################
#<palindfrome> ::= aa | ... | zz | AA | ... | ZZ | a<palindrome>a | ... | Z<palindrome?Z | letter  #
#<letter> ::= a | ... | z | A | ... | Z | ' ' | ∈                                                  #
####################################################################################################

#Remove Whitespaces if there are any
def removeSpace(string): 
    return string.replace(" ", "")
#Checks if string consists of only letters
def letterCheck(string):
    check = string.isalpha()

    if(check):
        pass
    else:
        print("Palindromes are composed of letters only!")
        quit()
#Checks if the string is palindrome
def palCheck(string):
    check = True

    for i in range(len(string)//2):
        if string[i] != string[len(string) - i - 1]:
            check = False
    
    return check

userInput = input("Enter String: ")
checkOne = removeSpace(userInput)
letterCheck(checkOne)
checkTwo = palCheck(checkOne)
if checkTwo == True:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Palindrome: pop, pop a pop, a but tuba
#Not a palindrome: hey, joe, the quick brown fox