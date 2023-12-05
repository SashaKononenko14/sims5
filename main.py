#створення симуляції життя
class Human:
    def __int__(self, name = "Human",
                job = None,
                home = None,
                car = None):
        self.name = name
        self.money = 50_000
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home