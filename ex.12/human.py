class Human:
    def __init__(self, name):
        self.name = name
        self.age = 0
        print(f"Родился человек с именем {self.name}")
        

    def eating(self):
        print(f"{self.name} питается")

    def sleeping(self):
        print(f"{self.name} спит")

    def working(self):
        if 18 <= self.age < 65:
            print(f"{self.name} работает")
        if self.age >= 65:
            print(f"{self.name} на пенсии")
        
    def relaxing(self):
        print(f"{self.name} отдыхает")

    def growing(self):
        self.age += 1
        print(f"{self.name} отмечает день рождения, ему уже {self.age} !")

class Life:
    def life(self, human, years=70):
        while years:
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1
        
grisha = Human('Гриша')
life_grisha = Life()
life_grisha.life(grisha)
