'''

Created on 2017/07/28 for Incarnation 1

@author Ahmed Squalli Houssaini


'''

' Importing only the debugger library '
import pdb

class Mathematics:
    ' Common class for basic mathematical functions needed for CHEERS'
    def __init__(self):
        self.__pi = self.Pi()
        
    def Pi(self):
        """Returns the value of pi."""
        pi = float(0)
        k = 0
        n = 100
        while k < n:
            pi += (float(1)/(16**k))*((float(4)/(8*k+1))-(float(2)/(8*k+4))-(float(1)/(8*k+5))-(float(1)/(8*k+6)))
            k += 1
        return pi
   
    def GetPi(self):
        return self.__pi
    
    def factorial(self, n):
        """Returns the value of factorial(n)."""
        if n<1:
            return 1
        else:
            return n * self.factorial(n-1)
    
    def cos(self, x):
        """Returns the value of cos(x)."""
        k = 0
        cos = float(0)
        while k < 10:
            cos+=((-1)**k)*(x**(2*k))/self.factorial(2*k)
            k+=1
        return cos

    def sin(self,x):
        """Returns the value of sin(x)."""
        k = 0
        sin = 0
        while k < 10:
            sin+=((-1)**k)*(x**(1+2*k))/self.factorial(1+2*k)
            k+=1
        return sin    

    def Newton(self,f, dfdx, x, eps):
        """
        Returns the root of the equation x - sin(x) = pi/2
        Using Newton's method
            
        """
        fx = f(x)
        counter = 0
        while abs(fx) > eps and counter < 100: # continue to iterate until decent result is obtained
            try:
                x = x - float(fx)/dfdx(x)
            except ZeroDivisionError:
                print "Error: Derivative is equal to zero for x = ", x
    
            fx = f(x)
            counter += 1 # Increment counter after one iteration
    
        return x
    
    def f(self,x):
        """Returns the function x - sin(x) - pi/2."""
        return x -  self.sin(x) - (self.__pi/ float(2.0))
    
    def dfdx(self,x):
        """Returns the derivative of the function x - sin(x) - pi/2."""
        return 1 - self.cos(x)





class Cheers:
    ' CHEERS class'
    def __init__(self, m):
        self.__precision = 1.0e-6
        self.__xStart = 3
        self.__math = m
        
    def computeAlpha(self):
        return self.__math.Newton(self.__math.f, self.__math.dfdx, self.__xStart, self.__precision)
    
    def computeL(self, R, alpha):
        L = 2*R*(1 - self.__math.cos(alpha/2))
        return L
    
    
math  = Mathematics()
cheers = Cheers(math)

alpha = cheers.computeAlpha()
radius = input("Please specify the value of R: ")
length = cheers.computeL(radius, alpha)
#pdb.set_trace()


print("Value of R: " +str(radius));
print("Value of L: " +str(length));