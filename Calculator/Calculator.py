from Calculator.Addition import addition
#from Calculator.Subtraction import subtraction
#from Calculator.Multiplication import multiplication
#from Calculator.Division import division
#from Calculator.Square import square
#from Calculator.Square_Root import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, num1, num2):
        self.result = addition(num1, num2)
        return self.result
