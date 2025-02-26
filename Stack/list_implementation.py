class stack:

    #This is a constructor
    def __init__(self) -> None:
        self.stack =[]

    #Push Operation
    def push(self, value):
        self.stack.append(value)

    #Pop Operation
    def pop(self):
        self.stack.pop()

    #printing result
    def printResult(self):
        return self.stack
    

s = stack()
s.push(30)
s.push(10)
s.push(20)
s.push(50)
print(s.printResult())
s.pop()
s.pop()
print(s.printResult())


        