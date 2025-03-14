#Deros
#=====


from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Func1:


    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def solving(self):
        ans = []
        d = ((self.b) ** 2) - (4 * self.c)

        if d < 0:
            print('Wrong data')
        elif d == 0:
            x = (-(self.b)) / (2 * self.a)
            ans.append(x)
        elif d > 0:
            x1 = ((-(self.b)) - sqrt(d)) / (2 * self.a)
            x2 = ((-(self.b)) + sqrt(d)) / (2 * self.a)
            ans.append(x1)
            ans.append(x2)
        
        return ans
    
    def func(self, x):
        y = (self.a * (x ** 2)) + (self.b * x) + self.c
        return y 

    def paint(self):
        # Интервал изменения переменной по оси X
        xmin = -20.0
        xmax = 20.0
        count = 200

        fig, self.ax = plt.subplots()

        self.xlist = np.linspace(xmin, xmax, count)
        ylist = [self.func(x) for x in self.xlist]
        self.ax.plot(self.xlist, ylist, color = 'red')
        self.ax.grid()
    
    def show(self):
        self.paint()
        plt.show()
    
    def __del__(self):
        print('Equation(x ** 2) has been deleted')


class Func2(Func1):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def func2(self, x):
        y = (self.a * x * 2) + self.b
        return y
    
    def paint(self):
        super().paint()
        ylist = [self.func2(x) for x in self.xlist]
        self.ax.plot(self.xlist, ylist, color = 'blue')
    
    def show(self):
        self.paint()
        plt.show()

    
    def __del__(self):
        print('Equation(x) has been deleted')


class Func3(Func1):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def func3(self, x):
        y = ((self.a * (x ** 3))/3) + ((self.b *(x ** 2))/2) + (self.c * x) + self.d
        return y
    
    def paint(self):
        super().paint()
        ylist = [self.func3(x) for x in self.xlist]
        self.ax.plot(self.xlist, ylist, color = 'yellow')
    
    def show(self):
        self.paint()
        plt.show()

def left():
    a, b, c  = int(input('Введите a:\n')), int(input('b:\n')), int(input('c:\n'))
    frs = Func1(a, b, c)
    print(frs.solving())
    frs.show()

def right():
    a, b, c  = int(input('Введите a:\n')), int(input('b:\n')), int(input('Введите c:\n'))
    nas = Func2(a, b, c)
    nas.show()

def up():
    a, b, c, d  = int(input('Введите a:\n')), int(input('b:\n')), int(input('Введите c:\n')), int(input('Введите d:\n'))
    nas2 = Func3(a, b, c, d)
    nas2.show()



def main():
    usr_choose =  input('Enter 1 if you want to see the parent class, and 2 if you want to see the child class, and 3 if you want to see second child classs \n')
    if usr_choose == '1':
       left()
    elif usr_choose == '2':
       right()
    elif usr_choose == '3':
        up()
    else:
       print('Ты это, жми правильные кнопки, а не неправильные ')

if __name__ == '__main__':
    main()


            
        