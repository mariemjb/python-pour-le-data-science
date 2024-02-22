def somme(x,y):
    return x+y
import math
class Point:
    #x=10 #attribut statique
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    def afficher(self):
        print("Point",self.x,self.y)
    def __str__(self):
        return "Point:"+str(self.x)+","+str(self.y)
    def decaler(self,P):
        self.x=self.x+P.x
        self.y =self.y+P.y
    def distance(self,P):
        dx=(self.x-P.x)
        dy=(self.y-P.y)
        d=(dx**2+dy**2)
        d2=math.sqrt(d)
        return d2