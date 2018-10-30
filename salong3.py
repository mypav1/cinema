class salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats


    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

r1 = salong("Svea", "140 poäng", 200)

class salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats


    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

r2 = salong("Thor", "100 poäng", 150)



class salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats


    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

r3 = salong("Greta", "80 poäng", 100)






r1.introduce_self()
r2.introduce_self()
r3.introduce_self()


def main():
    pass


if __name__ == '__main__':  # double underscore (dounder)
    main()