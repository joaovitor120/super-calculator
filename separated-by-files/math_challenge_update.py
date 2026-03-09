import random
from sympy import isprime
import time
 
levels = ['1','2','3','4']
levels_qtd = len(levels)
calc_types = ['1','2']

operations_type = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
    "**": lambda a,b: a ** b
}

operations_list = list(operations_type.keys())
operations_list_length = len(operations_list)

class DifficultyRange:
    def __init__(self):
        self.ranges = {
            "easy": {"min": 2, "med": 10, "max": 20},
            "medium": {"min": 11, "med": 20, "max": 50},
            "hard": {"min": 21, "med": 30, "max": 80},
            "very hard": {"min": 31, "med": 40, "max": 100}
        }
    
    def get_min(self, difficulty):
        return self.ranges[difficulty]["min"]
    
    def get_med(self, difficulty):
        return self.ranges[difficulty]["med"]
    
    def get_max(self, difficulty):
        return self.ranges[difficulty]["max"]
    def get_all(self, difficulty):
        return self.ranges[difficulty]
    
ranges = DifficultyRange()

"""index_easy_list = ranges.get_all("easy")
index_medium_list = ranges.get_all("medium")
index_hard_list = ranges.get_all("hard")
index_veryhard_list = ranges.get_all("very hard")"""

def ensure_option_menu_correctly(user_input,message_input,options_available): #ensure a valid input
    options_available_to_use = ('/'.join (i for i in options_available))
    while user_input not in options_available:
        print(f"This option is not available, please choose one option among them({options_available_to_use}) ")
        user_input = input(message_input)
    return user_input

def get_levels_difficulty(): #get inputs
    print("""1 - Simple operations(with only two numbers)
2 - Complex operations(with more than two numbers)
""")   
    message_input_calc_complex = "Choose one operation among them(1/2) to continue: "
    calculation_complexity_input = input(message_input_calc_complex).strip()
    options_available_calc = ['1', '2']
    calculation_complexity = ensure_option_menu_correctly(calculation_complexity_input, message_input_calc_complex, options_available_calc)
    print("""1 - Easy
2 - Medium
3 - Hard
4 - Very Hard
""")
    options_available_level = ['1', '2', '3', '4']
    level_difficult_message = "Choose one level difficult among them(1/2/3/4): "
    level_difficult_input = input(level_difficult_message).strip()
    level_difficult = ensure_option_menu_correctly(level_difficult_input, level_difficult_message, options_available_level)
    return calculation_complexity, level_difficult

def select_random_non_prime(range_min, range_max):
    """Select a random non-prime number within a given range."""
    # Create a list of all non-prime numbers in the range
    non_primes = [n for n in range(range_min, range_max) if not isprime(n)]    
    if non_primes == []:
        return random.randint(range_min, range_max)
    else:
        # Select a random non-prime from the list using the random.choice function
        return random.choice(non_primes)

def get_calculator_datas(range_min, range_med, range_max, index_min, index_max):
    num1 = select_random_non_prime(range_med,range_max)
    if range_min > 10 and range_med > 20:
        range_min = int(range_min // 2.3)
        range_med = int(range_med // 2)
    num2 = select_random_non_prime(range_min,range_med)
    op_symbol = random.choice((operations_list)[index_min:index_max])
    return num1, num2, op_symbol

def ensure_integer_result_simple(result, num1,num2, op_symbol,index_min, index_med, op_index_min, op_index_max):
    if not isinstance(result, int):
        numbers = list(range(index_min, index_med))
        if op_symbol == "/":
            validates_num2 = [i for i in numbers if num1 % i == 0]
            if validates_num2:
                num2 = random.choice(validates_num2)
                result = operations_type[op_symbol](num1,num2)
            else: #if not numbers options for num2 --> choose another op_symbol and num2
                while isinstance(result, int) == False:  #isistance return only True or False
                    op_symbol = random.choice((operations_list)[op_index_min:op_index_max])
                    result = operations_type[op_symbol](num1, num2)
                    if isinstance(result, int):
                        break
                    else:
                        num2_options = [i for i in numbers if isinstance((operations_type[op_symbol](num1, i)), int)]
                        if num2_options:
                            num2 = random.choice(num2_options)
                            result = operations_type[op_symbol](num1, num2)
    return num2, op_symbol, result

def force_expoent_two(result, num1,num2,op_symbol, index_med, index_max):
        if op_symbol == "**" and num2 != 2:
            num1 = select_random_non_prime(int(index_med // 2.5),int(index_max // 3))
            num2 = 2
            result = operations_type[op_symbol](num1, num2)
        return num1,num2,result
def validate_calculation(answer, correct_answer):
    if answer == correct_answer:
        return True #use this text to continue the proccess
    else:
        return False #use this flag to get a new input 
    
def answer_retry_loop(num1,num2, op_symbol,result_calc, result, multiple_operations=False):
    answer_status = validate_calculation(result_calc, result)
    while answer_status == False:
        print("Wrong answer, try again: ")
        if multiple_operations:
            try:
                result_calc = int(input(multiple_operations))
            except ValueError:
                print("Please, type an integer value: ")
        else:
            result_calc = int(input(f"{num1} {op_symbol} {num2} = "))

def generate_challenge(difficulty, op_min, op_max):
    print(difficulty)
    print(type(op_max))
    print(type(op_min))
    num1, num2, op_symbol = get_calculator_datas(ranges.get_min(difficulty), ranges.get_med(difficulty), ranges.get_max(difficulty),op_min,op_max)
    result = operations_type[op_symbol](num1, num2)
    num2, op_symbol, result = ensure_integer_result_simple(result,num1,num2,op_symbol,ranges.get_min(difficulty), ranges.get_med(difficulty),op_min,op_max)
    num1, num2, result = force_expoent_two(result, num1,num2,op_symbol, ranges.get_med(difficulty), ranges.get_max(difficulty))
    return num1, num2, op_symbol, result

def init_timer():
    start_time = time.perf_counter()  
    return start_time
def end_timer():
    end_time = time.perf_counter()
    return end_time
def ask_question(num1,num2,op_symbol, expression=None):
    if expression:
        result_calc = int(input(expression))
    else:
        result_calc = int(input(f"{num1} {op_symbol} {num2} = "))
    return result_calc

def challenge_simple(difficulty, op_min, op_max):
    num1, num2, op_symbol, result = generate_challenge(difficulty, op_min, op_max)
    result_calc = ask_question(num1,op_symbol,num2)
    start_time = init_timer()
    if result_calc != result:
        answer_retry_loop(num1,num2,op_symbol,result_calc,result)                    
    end_time = end_timer()
    execution_time = end_time - start_time
    print(f"Perfect, you answered correctly in {int(execution_time)} seconds, congratulations!")
    
def challenge_complex(difficulty, op_min, op_max):
    num1, num2, op_symbol, result = generate_challenge(difficulty, op_min, op_max)
                    
    num3, num4, op_symbol_1, result_1 = generate_challenge(difficulty, op_min, op_max)
    if op_max == operations_list_length:
        op_last_calc = op_max - 1
    op_symbol_2 = random.choice((operations_list)[op_min:op_last_calc])
    #print(op_symbol_2)
    final_result = operations_type[op_symbol_2](result, result_1)
    result_1, op_symbol_2, final_result = ensure_integer_result_simple(final_result,result,result_1,op_symbol_2,ranges.get_min(difficulty), ranges.get_med(difficulty),op_min, op_max)
    #print(op_symbol_2)
    if op_symbol_2 == "**":
        op_symbol_2 = random.choice((operations_list)[op_min:4])
        final_result = operations_type[op_symbol_2](result, result_1)
    expression = f"({num1} {op_symbol} {num2}) {op_symbol_2} ({num3} {op_symbol_1} {num4}) = "

    start_time = init_timer()                           
    result_calc = ask_question(expression=expression)
    if result_calc != final_result:
        answer_retry_loop(result,result_1,op_symbol_2,result_calc,final_result,expression) 
    end_time = end_timer()
    execution_time = end_time - start_time
    print(f"Perfect, your answer correctly in {int(execution_time)} seconds, congratulations!") 

op_index = {
    'easy': (0,4),
    'medium': (2,4),
    'hard': (2, operations_list_length),
    'very hard': (2, operations_list_length)
}

difficulty_map = {'1': "easy", '2': "medium", '3': "hard", '4': "very hard"}

def math_challenges():
    green_flag = True
    while green_flag == True:
        calc_type_complex, difficult = get_levels_difficulty()
        
        op_min, op_max = op_index[difficulty_map[difficult]]
        if calc_type_complex == '1':                                
                challenge_simple(difficulty_map[difficult], op_min, op_max)

        if calc_type_complex == '2':
                challenge_complex(difficulty_map[difficult], op_min, op_max)
        return_to_menu_msg = 'Do you want to return to main menu to execute another functions(Y/N)? '
        return_to_menu_input = input(return_to_menu_msg).upper().strip()
        return_to_menu_msg_options = ['Y', 'N']
        return_to_menu = ensure_option_menu_correctly(return_to_menu_input, return_to_menu_msg, return_to_menu_msg_options)
        if return_to_menu == 'Y':
            green_flag = False
#separate functions that make more than one function