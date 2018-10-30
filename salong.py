class Salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats

    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

s1 = Salong("Svea", "140 poäng", 200)
s2 = Salong("Thor", "100 poäng", 150)
s3 = Salong("Greta", "80 poäng", 100)

s1.introduce_self()
s2.introduce_self()
s3.introduce_self()


#class Filmer
    #def __init__(self):
        #self.name = name
        #self. =
        #self. =


#en ny meny som kopplas till den här menun sen så från den menun
#  jag gör ska man välja en specifik salong och
# då ska man få upp info om salongen och lite om filmen