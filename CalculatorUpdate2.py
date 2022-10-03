# package calculator

from math import nan
from enum import Enum

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"

class Trans:
    operator_dict = {"^": 3,
                     "*": 2,
                     "/": 2,
                     "+": 1,
                     "-": 1,
                     # "(": 0,
                     # ")": 8
                     }
    parenthesis_dict = {
        "(": 1,
        ")": 0
    }

    operator_assoc = {"^": 1,  # right
                      "*": 0,  # left
                      "/": 0,
                      "+": 0,
                      "-": 0,
                      "(": 0,
                      ")": 0,
                      }

    #test1 = input("yäni")
    swag=[]
    b=0
    stack = []
    output_queue = []
    #current_equation=None

    # if it is an operand we push it to the output queu
    def operand_check(self, element,current_equation):
        if (element not in Trans.operator_dict.keys()) and (element not in Trans.parenthesis_dict.keys()):
            Trans.swag.append(element)
        elif (element in Trans.operator_dict.keys()) or (element in Trans.parenthesis_dict.keys()):
            if len(Trans.swag) > 0:
                Trans.output_queue.append("".join(Trans.swag))
                Trans.swag.clear()
        if (element not in Trans.parenthesis_dict.keys()) and Trans.b == (len(current_equation)):
            if len(Trans.swag) > 1:
                Trans.output_queue.append("".join(Trans.swag))
            else:
                Trans.output_queue.append(element)


    def if_paranthesis(self,element):
        # push down the left parenthesis
        if element == "(":
            Trans.stack.append(element)
        # if it's right parenthesis then pop everything out of stack until
        # you reach left parenthesis
        elif element == ")":
            while Trans.stack[-1] != "(":
                temp = Trans.stack.pop()
                Trans.output_queue.append(temp)
            # to remove left parenthesis
            Trans.stack.pop()


    def if_operator(self,element):
        if element in Trans.operator_dict.keys():
            while (len(Trans.stack) != 0) and self.if_associative(element) and self.does_top_of_stack_have_operator():
                temp = Trans.stack.pop()
                Trans.output_queue.append(temp)
            Trans.stack.append(element)


    def if_associative(self,element):
        if Trans.stack[-1] == "(" or ((Trans.operator_assoc[element] == 0) and (Trans.operator_dict[element] <= Trans.operator_dict[Trans.stack[-1]])):
            return True
        elif Trans.stack[-1] == "(" or ((Trans.operator_assoc[element] == 1) and (Trans.operator_dict[element] < Trans.operator_dict[Trans.stack[-1]])):
            return True
        else:
            return False


    def does_top_of_stack_have_operator(self):
        return True if Trans.stack[-1] in Trans.operator_dict.keys() else False


    def empty_stack(self):
        while len(Trans.stack) != 0:
            temp = Trans.stack.pop()
            Trans.output_queue.append(temp)
            temp = []

    # main stream
    def run(self, current_equation):
        Trans.output_queue.clear()
        Trans.swag.clear()
        Trans.stack.clear()
        Trans.b = 0
        print(Trans.output_queue)
        for element in current_equation:
            print(current_equation)
            Trans.b+=1
            self.operand_check(element,current_equation)


            self.if_paranthesis(element)

            self.if_operator(element)

        #print("stack:", stack)
        #print("output queu", output_queu)
        # sleep(0.5)

        self.empty_stack()

        #print("stack:", Trans.stack)
        #print("output queue", Trans.output_queue)
        print("output queue", Trans.output_queue)
        output_queue = Trans.output_queue
        return output_queue

x = Trans()



def infix_to_postfix(current_equation):
    output_queue = x.run(current_equation)
    return output_queue  # TODO


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    stack=[]
    for c in postfix_tokens: # Appendar tal tills det kommer en "charachter" och utför då operationen på de två senaste talen, pga polish notation.
        if c == "+":
            #print(stack.pop())
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b  = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif c == "^":
            x, y = stack.pop(), stack.pop()
            g=y
            for i in range(x-1):
                g=g*y
            stack.append(g)
        else:
            stack.append(int(c))
    return stack[0]



# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    postfix_tokens = infix_to_postfix(expr)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str):
    return None   # TODO

# TODO Possibly more methods