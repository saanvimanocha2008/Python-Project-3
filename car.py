class Car:
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("Started")
    
    def stop(self):
        print("Stopped")
    
    def accelerate(self):
        print("Accelerated")
    
    def gear_change(self, gearType):
        print("Gear changed", gearType)
    
audi = Car("a6", "white", "audi", 80)
print(audi.color)
audi.accelerate()
audi.gear_change(5)

        