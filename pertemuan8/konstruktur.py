class Kalkulator: # membuat class Kalkulator
    def __init__(self,x,y): # ini disebut class constructor
        self.A = x # argument x dijadi class attribute A
        self.B = y # argument y dijadi class attribute B
        print ("A="+str(x)+",B="+str(y))
