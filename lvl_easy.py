import random
import operator
from typing import Tuple

def generate_question() -> Tuple[str, float]:
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    while True:
        oper = random.choice(list(operators.keys()))
        
        if oper == '/':
            num1 = random.randint(0, 99)
            num2 = random.randint(1, 9)
            if num1 % num2 != 0:
                continue
        elif oper == '-':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, num1)
        else:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
        
        answer = operators[oper](num1, num2)
        return f"{num1} {oper} {num2}", answer

if __name__ == "__main__":
    print(generate_question())
