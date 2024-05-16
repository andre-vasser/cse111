def say_hi():
    print('Hello!')

class Greeter:
    def __init__(self,msg):
        self.msg = msg

    def say_hi(self):
        print(self.msg)   


say_hi()
g1 = Greeter('Howdy')
g2 = Greeter('*Help me*')
g1.say_hi()
g2.say_hi()