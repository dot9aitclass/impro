# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def __whoisThis(self):
        print("Bird")

    def __swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
#peggy.swim()
peggy.run()
mc=Bird()
print (mc.__dict__)