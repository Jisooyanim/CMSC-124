import tokenize
from io import StringIO
from collections import deque

class Expression :

    # Set the precedence level of the operators
    precedence = {"^" : 4,  
                  "/" : 3,
                  "*" : 3,
                  "+" : 2,
                  "-" : 2,
                  "(" : 1 } 

    def __init__(self, exp_str) :
        self.exp_str = exp_str
        self.infix_tokens = []  
        self.postfix_tokens = []  

    def Evaluate(self) :
        self.Tokenize()
        self.InfixToPostfix()
        self.EvaluatePostfix()

    def Tokenize(self) :

        tuplelist = tokenize.generate_tokens(StringIO(self.exp_str).readline)

        for x in tuplelist :
            if x.string :
                self.infix_tokens.append(x.string)

        print("\nExpression : " + self.exp_str) #reprints input

    def InfixToPostfix(self) :

        stack = deque()
        stack.appendleft("(")
        self.infix_tokens.append(")")
    
        while self.infix_tokens :
    
             token = self.infix_tokens.pop(0) 

             if token == "(" :
                 stack.appendleft(token)

             elif token == ")" :
                 # Pop out all the operators from the stack and append them to 
                 # postfix expression till an opening bracket "(" is found

                 while stack[0] != "(" : # peek at topmost item in the stack
                     self.postfix_tokens.append(stack.popleft())
                 stack.popleft()

             elif token == "*" or token == "/" or token == "+"\
                 or token == "-" or token == "^" :

                 # Pop out the operators with higher precedence from the top of the
                 # stack and append them to the postfix expression before
                 # pushing the current operator onto the stack.
                 while ( stack and self.precedence[stack[0]] >= self.precedence[token] ) : 
                     self.postfix_tokens.append(stack.popleft())
                 stack.appendleft(token)

             else :
                 # Positions of the operands do not change in the postfix
                 # expression so append an operand as it is to the postfix expression
                 self.postfix_tokens.append(token)
    
        print("Postfix expression : ", end=' ')
        for token in self.postfix_tokens :
            print(token, end=',') #Tokenized Postfix Expression

    def EvaluatePostfix(self) :

        stack_result = deque()
    
        while self.postfix_tokens :
            token = self.postfix_tokens.pop(0)

            if token.isdigit() :
               stack_result.appendleft(float(token))
            else :
               x = float(stack_result.popleft())
               y = float(stack_result.popleft())

               # Note the order of operands(x, y), result equals [y(operator)x]
               if (token == "+") :
                   stack_result.appendleft(float(y+x))
               elif (token == "-") :
                   stack_result.appendleft(float(y-x))
               elif (token == "*") :
                   stack_result.appendleft(float(y*x))
               elif (token == "/") :
                   stack_result.appendleft(float(y/x))
               elif (token == "^") :
                   stack_result.appendleft(float(pow(y,x)))
    
        print("\n"+self.exp_str + " = " + str(stack_result.popleft()))

def main() :
    userInput = input("Expression: ")
    expr = Expression(userInput)
    expr.Evaluate()
   
if __name__ == "__main__" :
    main()