class Man:
    def __init__(self,name):
        self.name = name
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()

#걍 혼공파하고 할 걸 그랬나.. 이해가 안가네