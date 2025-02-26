class stack:
    #This is a constructor
    def __init__(self) -> None:
        self.stack = []

    #Push Operation
    def push(self, value):
        self.stack = [value] + self.stack

    #Pop Operation
    def pop(self):
        self.stack.pop(0)

    #Printing Result
    def printResult(self):
        return self.stack
    

s = stack()
s.push(80)
s.push(20)
s.push(40)
s.push(50)
s.push(70)
print(s.printResult())
s.pop()
print(s.printResult())
s.push(23)
print(s.printResult())