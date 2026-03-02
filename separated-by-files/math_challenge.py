from fractions import Fraction
import math
import random
import operator 

levels = [1,2,3,4]
calc_types = [1,2]
operations_type = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow
}
def get_level_difficult():

    print("""1 - Simple operations(with only two numbers)
2 - Complex operations(with more than two numbers)
""")
    calc_type_complex = int(input("Choose one operation among them(1/2) to continue: "))
    if calc_type_complex not in calc_types:
        calc_type_complex = int(input("Choose 1 or 2 to continue, please: "))
    print("""1 - Easy
2 - Medium
3 - Hard
4 - Very Hard
""")
    level_difficult = int(input("Choose one level difficult among them(1/2/3/4): "))
    if level_difficult not in levels:
        level_difficult = int(input("Choose a number between 1 and 4, please: "))
    return calc_type_complex, level_difficult

def math_challenges():
    calc_type_complex, difficult = get_level_difficult()
    match calc_type_complex:
        case 1:
            match difficult:
                case 1:
                    num1 = random.randint(10,20)
                    num2 = random.randint(1,10)
                    op_symbol = random.choice((list(operations_type.keys()))[:4])
                    result = operations_type[op_symbol](num1, num2)
                    while type(result) != int:
                        num2 = random.randint(1,10)
                        result = operations_type[op_symbol](num1, num2)
                        print("Choosing another number")
                    result_calc = int(input(f"{num1} {op_symbol} {num2} = "))
                    while result_calc != result:
                        print("Wrong answer, try again: ")
                        result_calc = int(input(f"{num1} {op_symbol} {num2} = "))
                    print("Perfect, your answer is correct, congratulations")

#continue the proccess tomorrow