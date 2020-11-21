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

