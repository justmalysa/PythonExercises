import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def sum_complex(self, complex2):
        return ComplexNumber(self.real + complex2.real, self.imag + complex2.imag)
    def diff_complex(self, complex2):
        return ComplexNumber(self.real - complex2.real, self.imag - complex2.imag)
    def multi_complex(self, complex2):
        return ComplexNumber(self.real*complex2.real - self.imag*complex2.imag, self.real*complex2.imag + self.imag*complex2.real)
    def abs_complex(self):
        return math.sqrt(self.real*self.real + self.imag*self.imag)

def complex_parse(string):
    arr = string.split("+")
    real_str = arr[0]
    imag_str = arr[1].strip("i")
    return int(real_str), int(imag_str)

operation = int(input("Give a operation to perform\n"
                  "1 - add complex numbers\n"
                  "2 - subract complex numbers\n"
                  "3 - multipliacte complex numbers\n"
                  "4 - abs of complex number\n"))

a = input("Give firts value in format x+yi\n")
real_a, imag_a = complex_parse(a)
complex_a = ComplexNumber(real_a, imag_a)

if operation != 4:
    b = input("Give second value in format x+yi\n")
    real_b, imag_b = complex_parse(b)
    complex_b = ComplexNumber(real_b, imag_b)

if operation == 1:
    result = complex_a.sum_complex(complex_b)
elif operation == 2:
    result = complex_a.diff_complex(complex_b)
elif operation == 3:
    result = complex_a.multi_complex(complex_b)
elif operation == 4:
    result = complex_a.abs_complex()

if  operation != 4:
    print("{}+{}i".format(result.real, result.imag))
else:
    print(result)


