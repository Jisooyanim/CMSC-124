from Problem_1 import Converter
from collections import deque

class InflixEvaluator:
    operations = ['+', '-', '/', '*', '^']

    def __init__(self):
        self.converter = Converter()
        self.postfixTokens = []
    
    def tokenizer(self, expression):
        expression = expression.split(' ')
        for char in expression:
            if char.isalnum() or char in self.operations:
                self.postfixTokens.append(char)
            if char == '//':
                self.postfixTokens.append('/')
                self.postfixTokens.append('/')
        return self.postfixTokens

    def evaluate(self, expression):
        type = self.converter.notation(expression)
        if type == "infix":
            expression = self.converter.convert(expression, type)[1]
            self.postfixTokens = self.tokenizer(expression)
            self.calculate(self.postfixTokens, 1)
        elif type == "prefix":
            self.calculate(expression, 2)
        elif type == "postfix":
            self.postfixTokens = self.tokenizer(expression)
            self.calculate(self.postfixTokens, 1)
        
    def calculate(self, tokens, mode):
        if mode == 1:
            stack = deque()
            while self.postfixTokens:
                token = self.postfixTokens.pop(0)
                if token.isdigit():
                    stack.appendleft(float(token))
                else:
                    stackOne = float(stack.popleft())
                    stackTwo = float(stack.popleft())

                    if token == '+':
                        stack.appendleft(float(stackTwo+stackOne))
                    elif token == '-':
                        stack.appendleft(float(stackTwo-stackOne))
                    elif token == '*':
                        stack.appendleft(float(stackTwo*stackOne))
                    elif token == '/':
                        stack.appendleft(float(stackTwo/stackOne))
                    elif token == '^':
                        stack.appendleft(float(pow(stackTwo,stackOne))) 
            print("Answer: " + str(stack.popleft()))
        
        if mode == 2:
            stack = []
            for char in tokens[::-1]:
                if char.isdigit():
                    stack.append(float(char))
                else:
                    stackOne = stack.pop()
                    stackTwo = stack.pop()
                    if char == '+':
                        stack.append(stackOne + stackTwo)
                    elif char == '-':
                        stack.append(stackOne - stackTwo)
                    elif char == '*':
                        stack.append(stackOne * stackTwo)
                    elif char == '/':
                        stack.append(stackOne / stackTwo)
            print("Answer: " + str(stack.pop()))

if __name__ == '__main__':
    get = Converter()
    eval = InflixEvaluator()
    userInput = input("Expression: ")
    type = get.notation(userInput)
    if type == 'prefix':
        userInput = userInput.replace(" ", "")
    eval.evaluate(userInput)

# References:
# https://www.algotree.org/algorithms/stack_based/evaluate_infix/ postfix evaluation
# https://www.geeksforgeeks.org/evaluation-prefix-expressions/ prefix evaluation