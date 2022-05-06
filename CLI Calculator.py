from cmath import log


class calculator:
    def __init__(self, first, second):
            
            self.first = first
            self.second = second    
    def add(self):
        answer = first + second
        calculator.output(answer)
    def multiply(self):
        answer = first * second
        calculator.output(answer)
    def divide(self):
        answer = first / second
        calculator.output(answer)
    def subtract(self):
        answer = first - second
        calculator.output(answer)
    def modulus(self):
        answer = first % second
        calculator.output(answer)
    def logarithm(self):
        answer = log(first, second)
        calculator.output(answer)
    def output(answer):
        print(f"The answer is:\t{answer}")
while True:
    first = float(input("Enter first number\t"))
    second = float(input('Input second number\t'))
    operation = input("Which operation do you want to perform?\nUse either the name or sign\n")
    calc = calculator(first, second)
    if 'add' in operation or '+' in operation:
        calc.add()
    elif 'sub' in operation or '-' in operation:
        calc.subtract()
    elif 'div' in operation or '/' in operation:
        calc.divide()
    elif 'mul' in operation or '*' in operation:
        calc.multiply()
    elif 'mod' in operation or '%' in operation:
        calc.modulus()
    elif 'log' in operation:
        calc.logarithm()
    else:
        print("Please select a valid operation\n")

    calculate_again = input("Would you like to continue using the calculator? y/N: ").lower()
    if "y" not in calculate_again:
        exit()