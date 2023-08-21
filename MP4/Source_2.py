import string
from Source_1 import NotationConverter

class InflixEvaluator:
    operations = ['+', '-', '/', '*', '^']

    def __init__(self) -> None:
        self.converter = NotationConverter()
        self.index: int = 0

    def evaluate(self, expression):
        operands = expression.split(' ')
        keys = string.ascii_lowercase
        
        symbols = {}

        for i in range(0, len(operands)):
            if operands[i].isnumeric():
                if i < 27:
                    symbols[keys[i]] = operands[i]
                else:
                    symbols[keys[i]*i] = operands[i]

        notation = self.converter.identify(expression)

        if notation == 1:
            expression = "({})".format(expression)
        elif notation == 2:
            expression = self.converter.convert(expression, notation)[0]
        elif notation == 3:
            expression = self.converter.convert(expression, notation)[0]
        else:
            raise ValueError()

        return self.__calculate(expression.replace(' ', ''))[0]

    def __calculate(self, expression):
        expressions: list = []

        while self.index < len(expression):
            operand: str = ""

            if expression[self.index] == '(':

                self.lex()
                expressions += self.__calculate(expression)

            elif expression[self.index] == ')':
                self.lex()
                return expressions

            elif expression[self.index].isnumeric():

                while expression[self.index].isnumeric():
                    operand += expression[self.index]
                    self.lex()
                expressions.append(int(operand))

            elif expression[self.index] in self.operations:
                if expression[self.index] == '+':
                    self.lex()

                    while expression[self.index].isnumeric():
                        operand += expression[self.index]
                        self.lex()

                    if operand.isnumeric():
                        expressions = [expressions[-1] + int(operand)]
                    else:
                        expressions = [expressions[-1] + self.__calculate(expression)[-1]]
                elif expression[self.index] == '-':
                    self.lex()

                    while expression[self.index].isnumeric():
                        operand += expression[self.index]
                        self.lex()

                    if operand.isnumeric():
                        expressions = [expressions[-1] - int(operand)]
                        self.lex()
                    else:
                        expressions = [expressions[-1] -
                                       self.__calculate(expression)[-1]]

                elif expression[self.index] == '*':
                    self.lex()

                    while expression[self.index].isnumeric():
                        operand += expression[self.index]
                        self.lex()

                    if operand.isnumeric():
                        expressions = [expressions[-1] * int(operand)]
                        self.lex()
                    else:
                        expressions = [expressions[-1] * self.__calculate(expression)[-1]]

                elif expression[self.index] == '/':
                    self.lex()

                    while expression[self.index].isnumeric():
                        operand += expression[self.index]
                        self.lex()

                    if operand.isnumeric():
                        expressions = [expressions[-1] //
                                       int(operand)]
                        self.lex()
                    else:
                        expressions = [expressions[-1] // self.__calculate(expression)[-1]]

                elif expression[self.index] == '^':
                    self.lex()

                    while expression[self.index].isnumeric():
                        operand += expression[self.index]
                        self.lex()

                    if operand.isnumeric():
                        expressions = [expressions[-1] ** int(operand)]
                        self.lex()
                    else:
                        expressions = [expressions[-1] ** self.__calculate(expression)[-1]]
            else:
                raise ValueError()

        return expressions

    def lex(self) -> None:
        self.index += 1


if __name__ == '__main__':
    print("Input an expression to evaluate.", end='')
    try:
        evaluator = InflixEvaluator()
        str_expr = input("\n\nExpression: ")
        print("\n---Equivalent Output---\n\t\t{}\n".format(evaluator.evaluate(str_expr)))
    except ValueError:
        print("\n---No Equivalent Output---\n")
    except IndexError:
        print("\n---No Equivalent Output---\n")

###
# ((((6-(2+3))*(3+(8/2)))^2)+3) 
# (9+(2*6))
# ((7+(4*5))-(2+0))
# ((8+(6/3))-2)
# ( 5 + 10 ) / ( 20 / 4 )