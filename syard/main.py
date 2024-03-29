operators = ["+","-","/","*","^"]

expressions = []
expressions.append("( ( 10 + 2 ) * 5 ) / 10 * 10 * 10")
expressions.append("5 ^ ( ( 1 + 2 ) * 1 + 2 )")
expressions.append("5+5")


output_expression = []


class Stack:
    operator_stack=[]
    top = -1

    def push(self, pushee):
        self.operator_stack.append(pushee)
        self.top = self.top + 1
        
    def pop(self):        
        self.top = self.top - 1
        return self.operator_stack.pop()

    def atTop(self):
        return self.operator_stack[self.top]

    def isEmpty(self):
        return self.top == -1

def isOperator(incoming):
    if operators.count(incoming) is 0:
        return False
    else:
        return True

def isSymbol(incoming):
    symbols = operators+['(',')']
    if symbols.count(incoming) is 0:
        return False
    else:
        return True

def precedenceOf(incoming):
    if incoming == "+" or incoming == "-":
        return 1
    if incoming == "*" or incoming == "/":
        return 2
    if incoming == "^":
        return 3
    if incoming == ")" or incoming == "(":
        return 0

stacker = Stack()

def pre_tokenisation(incoming):
    incoming = incoming.replace(' ','')
    resultant = []
    x=0
    while x < len(incoming):
        if isSymbol(incoming[x]):
            resultant.append(incoming[x])
            x = x + 1
        else:
            holding = ''
            while (x < len(incoming) and (isSymbol(incoming[x]) is False)):
                holding = holding + incoming[x]
                x = x + 1
            resultant.append(holding)
    return resultant


def infix_postfix(expression):
    tokens = pre_tokenisation(expression)
    for token in tokens:
        if token == '(':
            stacker.push(token)
        elif token == ')':
            while (stacker.atTop() != '('):
                output_expression.append(stacker.pop())
            stacker.pop()
        elif isOperator(token):
            while (stacker.isEmpty() == False) and (precedenceOf(token) <= precedenceOf(stacker.atTop()) and (stacker.atTop() != '(')):
                output_expression.append(stacker.pop())
            stacker.push(token)
        else:
            output_expression.append(token) # Operands
    
    while stacker.isEmpty() == False:
        output_expression.append(stacker.pop())
    return output_expression

# print(" ".join(output_expression))




def operate(num1, num2, operation):
    if operation == '+':
        return num2 + num1
    if operation == '*':
        return num2 * num1
    if operation == '/':
        return num2 / num1
    if operation == '-':
        return num2 - num1
    if operation == '^':
        return num2**num1
    return 0

def post_fix_evaluation(postfix):
    intermediate_stack = Stack()
    for token in postfix:
        if isOperator(token):
            num1 = float(intermediate_stack.pop())
            num2 = float(intermediate_stack.pop())
            result = operate(num1, num2, token)
            intermediate_stack.push(result)
        else:
            intermediate_stack.push(token)
    return intermediate_stack.pop()


for expression in expressions:
    print( expression," = ", post_fix_evaluation( infix_postfix(expression)))
