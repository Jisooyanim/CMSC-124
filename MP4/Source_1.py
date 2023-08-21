from typing import List

class NotationConverter:
  chars = ['+', '-', '/', '*', '^']

  def identify(self, expr):
    str_position = {
      "lastchar" : expr[-1],
      "firstchar": expr[0]
    }

    if str_position["lastchar"] in self.chars: #postfix
      return 3
    elif str_position["firstchar"] in self.chars: #prefix
      return 2
    elif str_position["firstchar"].isalnum() or expr[0] == '(': #infix
      return 1
    else:
      return 0

  def convert(self, expr, type):
    if type == 1:
      return (self.toPrefix(expr, type), self.toPostfix(expr, type))
    elif type == 2:
      return (self.toInfix(expr, type), self.toPostfix(expr, type))
    elif type == 3:
      return (self.toInfix(expr, type), self.toPrefix(expr, type))
    else:
      raise ValueError("Invalid expression")

  """ Infix to Prefix """
  def toPrefix(self, expr, type):
    if type == 1:
      expr = "".join(reversed(expr.replace('(', '~').replace(')', '(').replace('~', ')')))
      return "".join(list(reversed(self.toPostfix(expr, type))))

    elif type == 3:                 # Postfix to Prefix
      i: int = 0
      stack: List[str] = []
      while i < len(expr):
        if expr[i] in self.chars:
          stack.append(''+expr[i]+stack.pop(-2)+stack.pop())
          i = self.lex(i)
        elif expr[i].isalnum():
          operand = expr[i]
          i = self.lex(i)
          if ' ' in expr and i < len(expr):
            while expr[i].isalnum():
              operand += expr[i]
              i = self.lex(i)
          stack.append(''+operand)
        elif expr[i].isspace():
          i = self.lex(i)
        else:
          raise ValueError()
      return "".join(stack[-1]).lstrip()
    else:
      raise ValueError()

  def toInfix(self, expr, type):
    if type == 2:                 # Prefix to Infix
      stack: List[str] = []
      i: int = len(expr) - 1
      while i >= 0:
        if expr[i] in self.chars:
          stack.append('('+stack.pop()+expr[i]+stack.pop()+')')
          i = self.rlex(i)
        elif expr[i].isalnum():
          operand = expr[i]
          i = self.rlex(i)
          if ' ' in expr and i >= 0:
            while expr[i].isalnum():
              operand += expr[i]
              i = self.rlex(i)
          stack.append(operand)
        elif expr[i].isspace():
          i = self.rlex(i)
        else:
          raise ValueError()
      return stack[-1]

    elif type == 3:               # Postfix to Infix
      stack: List[str] = []
      i: int = 0
      while i < len(expr):
        if expr[i].isalnum():
          operand = expr[i]
          i = self.lex(i)
          if ' ' in expr and i < len(expr):
              while expr[i].isalnum():
                  operand += expr[i]
                  i = self.lex(i)
          stack.append(operand)

        elif expr[i] in self.chars:
          stack.append('('+stack.pop(-2)+expr[i]+stack.pop()+')')
          i = self.lex(i)
        elif expr[i].isspace():
            i = self.lex(i)
        else:
            raise ValueError()
      return stack[-1]
    else:
        raise ValueError()

  def toPostfix(self, expr, type):  # Infix to Postfix
    if type == 1:
      expr = "({})".format(expr)
      postfix = ""
      stack: List[str] = ['~']
      i = 0
      while i < len(expr):
        if expr[i].isalnum():
          operand = expr[i]
          i = self.lex(i)
          if ' ' in expr and i < len(expr):
            while expr[i].isalnum():
              operand += expr[i]
              i = self.lex(i)
          postfix += '' + operand + ''
        elif expr[i] == '(':
          stack.append(expr[i])
          i = self.lex(i)
        elif expr[i] == ')':
          while stack[-1] != '(':
            postfix += stack[-1]
            stack.pop()
          stack.pop()
          i = self.lex(i)
        elif expr[i] in self.chars:
          if expr[i] == '^':
            while self.__identifyPriority(expr[i]) <= self.__identifyPriority(stack[-1]):
              postfix += stack[-1]
              stack.pop()
          else:
            while self.__identifyPriority(expr[i]) < self.__identifyPriority(stack[-1]):
              postfix += stack[-1]
              stack.pop()
          stack.append(''+expr[i])
          i = self.lex(i)
        elif expr[i].isspace():
          i = self.__lex(i)
        else:
          raise ValueError()
      return postfix.lstrip()

    elif type == 2:    # Prefix to Postfix
      stack: List[str] = []
      i: int = len(expr) - 1
      while i >= 0:
        if expr[i] in self.chars:
          stack.append(''+stack.pop()+stack.pop()+expr[i])
          i = self.rlex(i)
        elif expr[i].isalnum():
          operand = expr[i]
          i = self.rlex(i)
          if ' ' in expr and i >= 0:
            while expr[i].isalnum():
              operand += expr[i]
              i = self.rlex(i)
          stack.append(''+operand)
        elif expr[i].isspace():
          #stack.append(expr[i])
          i = self.rlex(i)
        else:
          raise ValueError()
      return stack[-1]
    else:
      raise ValueError()
            
  """ Identify order """
  def __identifyPriority(self, operator: str) -> int:
    if operator in {'+', '-'}:
        return 1
    elif operator in {'*', '/'}:
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

  def lex(self, index: int) -> int:
    return index + 1

  def rlex(self, index: int) -> int:
    return index - 1

def numbers_to_strings(argument):
  switcher = {
    1: "Infix",
    2: "Prefix",
    3: "Postfix",
  }
  return switcher.get(argument, "Invalid Notation")

if __name__ == '__main__':
  expr = ""
  print("Input an expression in infix, prefix, or postfix form.", end='')
  nconverter = NotationConverter()
  expr = input("\n\nExpression: ")
  identification = numbers_to_strings(nconverter.identify(expr))
  try:
    if identification == "Infix":
      print("\n---Equivalent Prefix & Postfix---\n\tPrefix  : {}\n\tPostfix : {}\n".format(*nconverter.convert(
      expr, nconverter.identify(expr))))
    elif identification == "Prefix":
      print("\n---Equivalent Infix & Postfix---\n\tInfix   : {}\n\tPostfix : {}\n".format(*nconverter.convert(
      expr, nconverter.identify(expr))))
    elif identification == "Postfix":
      print("\n---Equivalent Infix & Prefix---\n\tInfix  : {}\n\tPrefix : {}\n".format(*nconverter.convert(
      expr, nconverter.identify(expr))))
    else:
      print("\n---No Equivalent Notation---\n")
  except ValueError:
    print("\n---No Equivalent Notation---\n")
  except IndexError:
    print("\n---No Equivalent Notation---\n")