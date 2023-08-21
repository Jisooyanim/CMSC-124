class Converter: 
    operators = ['+', '-', '*', '/', '^']
    operatorswParanthesis = set(['+', '-', '*', '/', '(', ')', '^']) 
    operatorPrecedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    #Classify what kind of notation is the expression
    def notation(self, expression):
        if expression[-1] in self.operators:
            return "postfix"
        if expression[0].isalnum() or expression[0] == '(':
            return "infix"
        if expression[0] in self.operators:
            return "prefix"
        else:
            print("Invalid Expression")
            quit()
    #Converts expressions to Infix notation
    def toInfix(self, expression, type): #DONE
        if type == "prefix": #CHECK
            stack = []
            i = len(expression) - 1

            while i >= 0:
                if expression[i] in self.operators:
                    sub = "(" + stack.pop() + expression[i] + stack.pop() + ")"
                    stack.append(sub)
                    i -= 1
                else:
                    stack.append(expression[i])
                    i -= 1
            return stack.pop()
    
        elif type == "postfix": #CHECK
            stack = []
            i = 0
            while i < len(expression):
                if expression[i].isalnum():
                    operand = expression[i]
                    i += 1
                    if ' ' in expression and i < len(expression):
                        while expression[i].isalnum():
                            operand += expression[i]
                            i += 1
                    stack.append(operand)
                elif expression[i] in self.operators:
                    stack.append('(' + stack.pop(-2) + expression[i] + stack.pop() + ')')
                    i += 1
                elif expression.isspace():
                    i += 1
                else:
                    print("Cannot be converted!")
            return stack[-1]   

        else:
            print("Cannot be converted")  
    #Converts expressions to prefix notation
    def toPrefix(self, expression, type): #DONE
        if type == "infix": #CHECK
            expression = "".join(reversed(expression.replace('(', '~').replace(')', '(').replace('~', ')')))
            return "".join(list(reversed(self.toPostfix(expression, type))))
        
        elif type == "postfix": #CHECK
            stack = []
            for i in range(len(expression)):
                if expression[i] in self.operators:
                    stackOne = stack[-1]
                    stack.pop()
                    stackTwo = stack[-1]
                    stack.pop()

                    temp = expression[i] + stackTwo + stackOne
                    stack.append(temp)
                else:
                    stack.append(expression[i])
            prefix = ""
            for i in stack:
                prefix += i
            return prefix
        
        else:
            print("Cannot be converted")        
    #Converts expressions to postfix notation
    def toPostfix(self, expression, type):
        if type == "infix": #CHECK
            stack = []
            postfix = ''

            for i in expression:
                if i not in self.operatorswParanthesis:
                    postfix += i
                elif i == '(':
                    stack.append('(')
                elif i == ')':
                    while stack and stack[-1] != '(':
                        postfix += stack.pop()
                    stack.pop()
                else:
                    while stack and stack[-1] != '(' and self.operatorPrecedence[i] <= self.operatorPrecedence[stack[-1]]:
                        postfix += stack.pop()
                    stack.append(i)
            while stack:
                postfix += stack.pop()
            return postfix
    
        elif type == "prefix": #CHECK
            stack = []
            expression = expression[::-1]
            postfix = ''

            for i in expression:
                if i in self.operators:
                    stackOne = stack.pop()
                    stackTwo = stack.pop()

                    temp = stackOne + stackTwo + i
                    stack.append(temp)
                else:
                    stack.append(i)
            while stack:
                postfix += stack.pop()
            return postfix
        else:
            print("Cannot be converted") 
    #Function that is tasked to give the asked expressions
    def convert(self, expression, type):
        if type == "infix":
            return (self.toPrefix(expression, type), self.toPostfix(expression,type))
        if type == "prefix":
            return (self.toInfix(expression, type), self.toPostfix(expression, type))
        if type == "postfix":
            return (self.toInfix(expression, type), self.toPrefix(expression,type))
    
if __name__ == '__main__':
    userInput = input("Expression: ").replace(" ", "")
    conv = Converter()
    type = conv.notation(userInput)
    #print(type)

    if type == "infix":
        print("Prefix: {}\nPostfix: {}".format(*conv.convert(userInput, type)))
    if type == "prefix":
        print("Infix: {}\nPostfix: {}".format(*conv.convert(userInput, type)))
    if type == "postfix":
        print("Infix: {}\nPrefix: {}".format(*conv.convert(userInput, type)))

# References:
# https://www.geeksforgeeks.org/prefix-infix-conversion/ PREFIX TO INFIX
# https://www.geeksforgeeks.org/postfix-prefix-conversion/ POSTFIX TO PREFIX
# https://favtutor.com/blogs/infix-to-postfix-conversion#:~:text=How%20to%20Convert%20Infix%20to,match%20the%20order%20of%20operation. INFIX TO POSTFIX
# https://www.geeksforgeeks.org/prefix-postfix-conversion/ PREFIX TO POSTFIX