import Myro
import Graphics

class Interpreter:
    def __init__(self):
        self.operators = {'display': self.display, '+': self.add, '-': self.sub, '*': self.mult, '/': self.div, '**': self.exp, 'forward': self.forward, 'backward': self.backward, 'turnRight': self.turnRight, 'turnLeft': self.turnLeft, 'beep': self.beep, 'beep2': self.beep2, 'getLightLeft': self.getLightLeft, 'getLightCenter': self.getLightCenter, 'getLightRight': self.getLightRight, 'getRightIR': self.getRightIR, 'getLeftIR': self.getLeftIR, 'getBattery': self.getBattery, 'takePicture': self.takePicture, 'showPicture': self.showPicture, 'read': self.read, 'popOff': self.popOff, 'dup': self.dup, 'swap': self.swap}
        self.stack = []

    def display(self):
        v = self.stack.pop()
        print (v)
    
    def add(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v1 + v2)

    def sub(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v1 - v2)

    def mult(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v1 * v2)

    def div(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v1 / v2)

    def exp(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v1 ** v2)

    def forward(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.forward(v1,v2))

    def backward(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.backward(v1,v2))

    def turnRight(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.turnRight(v1,v2))

    def turnLeft(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.turnLeft(v1,v2))

    def beep(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.beep(v1,v2))

    def beep2(self):
        v3 = float(self.stack.pop())
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(Myro.beep(v1,v2,v3))

    def getLightLeft(self):
        self.stack.append(Myro.getLight('left'))

    def getLightRight(self):
        self.stack.append(Myro.getLight('right'))

    def getLightCenter(self):
        self.stack.append(Myro.getLight('center'))

    def getRightIR(self):
        self.stack.append(Myro.getIR('right'))

    def getLeftIR(self):
        self.stack.append(Myro.getIR('left'))

    def getBattery(self):
        self.stack.append(Myro.getBattery())

    def takePicture(self):
        self.stack.append(Myro.takePicture())

    def showPicture(self):
        if len(self.stack) == 0:
            self.takePicture()
        p = self.stack.pop()
        Myro.show(p)

    def read(self):
        fileName = self.stack.pop()
        file = open(fileName)
        for line in file.readlines():
            if line[0] != "#":
                i.interpret(line)

    def interpret(self, expression):
        for token in expression.split():
            if token in self.operators:
                operator = self.operators[token]
                operator()
            else:
                self.stack.append(token)

    def popOff(self):
        self.stack.pop()

    def dup(self):
        v = float(self.stack.pop())
        self.stack.append(v)
        self.stack.append(v)

    def swap(self):
        v2 = float(self.stack.pop())
        v1 = float(self.stack.pop())
        self.stack.append(v2)
        self.stack.append(v1)

i = Interpreter()

#to test put
#i.interpret('programname.yp read')
#into shell
