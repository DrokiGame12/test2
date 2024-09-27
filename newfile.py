class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_data(func):
    def wrapper(*numbers: int):
        print(f"{func.__name__}({','.join(map(str, numbers))}) = {func(*numbers)}")
    return wrapper

def debag_numbers(func):
    def wrapper(*numbers: int):
        for number in numbers:
            if type(number) != type(0):
                print(f'{colors.RED}[{colors.UNDERLINE}ERROR{colors.CLEAR}{colors.RED}] {func.__name__} - {number} not int{colors.CLEAR}')
                break
        else:
            func(*numbers)
    return wrapper

@debag_numbers
@print_data
def summ(*numbers: int):
    return sum(numbers)

@debag_numbers
@print_data
def mult(*numbers: int):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == '__main__':
    summ(0,1, 2, 3, 4)
    summ(5, 6, '7', 8)
    mult(1, 2, 3, '4')
    mult(5, 6, 7, 8)

