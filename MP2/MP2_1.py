#####################################BNF GRAMMAR#############################################
#<string> ::= <expression>                                                                  #
#<expression> ::= (<expression>) | <operation>                                              #
#<operation> ::= <expression> <sign> <expression> | <unary> <expression> | <identifier>     #
#<sign> ::= + | -                                                                           #
#<unary> ::= ~                                                                              #
#<identifier> ::= x | y | z                                                                 #
#############################################################################################

#Remove Whitespaces if there are any
def removeSpace(string): 
    return string.replace(" ", "")
#Checks if every open paranthesis have corresponding closing paranthesis
def paraCheck(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    
    if(count == 0):
        return True
    else:
        print("Uneven number of parantheses.")
        quit()
#Checks string if it is valid in BNF Grammar
def gramCheck(string):
    check = 1
    
    for i in range(len(string) - 1):
        cur = string[i]
        next = string[i + 1]

        if cur == '(':
            if next == 'x' or next == 'y' or next == 'z' or next == '~':
                pass
            else:
                check = 0
                break
        elif cur == '~':
            if next == 'x' or next == 'y' or next == 'z':
                pass
            else:
                check = 0
                break
        elif cur == 'x' or cur == 'y' or cur == 'z':
            if next == ')' or next == '+' or next == '-':
                pass
            else:
                check = 0
                break
        elif cur == '+' or cur == '-':
            if next == 'x' or next == 'y' or next == 'z' or next == '(' or next == '~':
                pass
            else:
                check = 0
                break
        
    return check

userInput = input("Enter string: ")
checkOne = removeSpace(userInput)
checkTwo = paraCheck(checkOne)
checkThree = gramCheck(checkOne)
if checkThree == 0:
    print(userInput + " isn't valid")
else:
    print(userInput + " is valid")

######Test Cases######
#Valid strings:      #
#   ~x+~y            #
#   (x+z-y)          #
#   z-(x+y)          #
#Invalid strings:    # 
#   a+b              #
#   xy-xz            #
#   z(x+y)           #
######################