class salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats


    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

s1 = salong("Svea", "140 poäng", 200)
s2 = salong("Thor", "100 poäng", 150)
s3 = salong("Greta", "80 poäng", 100)

s1.introduce_self()
s2.introduce_self()
s3.introduce_self()


