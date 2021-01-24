import math

class Complex:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def display(self):
        print(f"{self.x} + {self.y}i")

    def modulus(self):
        return (math.sqrt(self.x*self.x + self.y*self.y))

    def conjugate(self):
        self.y=-self.y
        return

    def inverse(self):
        self.x=self.x/(self.x*self.x + self.y*self.y)
        self.y=self.y/(self.x*self.x + self.y*self.y)
        return 




a=Complex(1,2)
a.display()

b=Complex(2,-3)
print(b.modulus())


b.conjugate()
b.display()

c=Complex(1,1)
d=Complex(2,5)
c.inverse()
d=c
d.display()






