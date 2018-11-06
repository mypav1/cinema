
class Movie_info:
    def __init__(self):
        self.svea = self.format_movie(self.movie_svea())
        self.greta = self.format_movie(self.movie_greta())
        self.thor = self.format_movie(self.movie_thor())

    def format_movie(self, text_list):
        result = "".join(text_list)
        result = result.replace(';', '\n')
        return result

    def movie_svea(self):
        with open("svea.txt", "r") as i:
            return i.readlines()

    def movie_thor(self):
        with open("thor.txt", "r") as i:
            return i.readlines()

    def movie_greta(self):
        with open("greta.txt", "r") as i:
            return i.readlines()


class Salons:
    def __init__(self,Salon1,Salon2,Salon3):
        self.salon1 = Salon1(name="Svea", points=140, seats=200)
        self.salon2 = Salon2(name="Thor", points=100, seats=150)
        self.salon3 = Salon3(name="Greta", points=80, seats=100)
        self.salons = [self.salon1, self.salon2, self.salon3]



    def __str__(self):
         return f"{self.salon1} har {self.salon2} platser och kostar {self.salon3} poäng"

    def print_movies(self):
        for i, salon in enumerate(self.salons):
            print("Salong", i + 1, salon)


class Person:
    def __init__(self, first="", last="", persno=0):
        self.firstname = first
        self.lastname = last
        self.personalnumber = persno

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.personalnumber}"

    def __repr__(self):
        return f"{self.firstname}, {self.lastname}, {self.personalnumber}"

class Person_Collection:

    def __init__(self):
        self.List_of_all_members = []

    def add_person(self, person):
        self.List_of_all_members.append(person)


    def print_list(self):
        return print(self.List_of_all_members)

class Saldo_Menu:
    def __init__(self,saldo=0, spenderade_point=0,bonus=0):
        self.saldo=saldo
        self.spenderade_point=spenderade_point
        self.bonus=bonus

    def __str__(self):
        return f"{self.saldo}, {self.spenderade_point}, {self.bonus}"

    def __repr__(self):
        return f"{self.saldo}, {self.spenderade_point}, {self.bonus}"


    def info (self):
        if self.saldo == 0:
            print("Tyvär du har inte tillräcklig med poäng!" + "--" + str(self.saldo) + "Kr")
            return self.saldo
        if self.spenderade_point == 0:
            return str(self.saldo)
        else:
            print(str(self.saldo) + "Kr har sparats")


class Point:

    def __init__(self):
        self.list_saldo = []

    def add_saldo(self,point):
        self.list_saldo.append(point)

    def print_saldo(self, spenderade_point,saldo):
        print(str(sum([value.saldo for value in self.list_saldo]) - spenderade_point) + "Kr har kvar i kontot")
        if spenderade_point>saldo:
            print("Tyvärr går ej handla mer än det som du har!")


    def print_list(self,point):
        for i in self.list_saldo:
           if i ==point:
               print(i.spenderade_point,"Poäng har du spenderat")

class Snack_menu:
   def __init__(self, snack=20):
       self.snack = snack


   def __str__(self):
       return f"{self.snack}, {self.p} points"

   def __repr__(self):
       return f"{self.snack}, {self.p} points"


class Drink_menu:
   def __init__(self, drink=20):
       self.drink = drink


   def __str__(self):
       return f"{self.drink}, {self.p} points"

   def __repr__(self):
       return f"{self.drink}, {self.p} points"

class Combo_menu(Drink_menu, Snack_menu):
   def __init__(self, drink=15, snack=15):
       Drink_menu.__init__(self, drink)
       Snack_menu.__init__(self, snack)


   def __str__(self):
       return f"{self.snack}, {self.drink}, {self.p} points"

   def __repr__(self):
       return f"{self.snack}, {self.drink}, {self.p} points"




def main():
    persons = Person_Collection()
    point = Saldo_Menu()
    points = Point()
    person = Person()
    snack = Snack_menu()
    drink = Drink_menu()
    combo = Combo_menu()
    movie=Movie_info()

    salong=Salons()
    while True:
        print("1. Skapa nytt konto:")
        print("2. Saldokollen:")
        print("3. Handla i kiosk")
        print("4. Kolla aktuella filmer")
        print("5. Avsluta programmet:")
        print("*" * 25)
        choise = int(input("Ange ditt val: "))
        print("*" * 25)

        if choise == 1:

            while True:
                try:
                    print("___________Menyval__________")
                    print("Tryck 1 för att spara personuppgifter")
                    print("Tryck 2 för att visa sparade personuppgifter")
                    print("Tryck 3 för att gå till huvudmenun!")
                    val1 = input("Val:")
                    val1 = int(val1)
                except ValueError:
                    print("Välj endast mellan 1 eller 2!")

                if val1 == 1:

                    person.firstname = input("Skriv in dit Förnamn")
                    person.lastname = input("Skriv in dit efternamn")
                    try:
                        personalnumber = input("Skriv in din personnumber")
                        person.personalnumber = int(personalnumber)
                        persons.add_person(person)

                    except ValueError:
                        print("Endast siffror!")

                    with open("Personregister.txt", "a")as f:
                        f.write(f"{person.firstname};{person.lastname};{person.personalnumber}\n")

                if val1 == 2:
                    persons.print_list()
                if val1==3:
                    break
        if choise == 2:



            print("___________MENU____________")
            print("1.Saldo")
            print("2.Spendering av poäng")
            print("3.Plånboken")
            print("4.Exit")

            while True:
                try:
                    chooise = input("Välj:__")
                    chooise = int(chooise)
                except ValueError:
                    print("Välj endast 1 eller 2!")
                if chooise == 1:
                    try:

                        point.spenderade_point = salong.Salon1.points.None
                        point.spenderade_point=salong.Salon1.name
                        point.spenderade_point=salong.Salon1.seats

                        points.print_saldo(point.spenderade_point, point.saldo)

                    except ValueError:
                        print("Summan i sifror endast!")
                if chooise == 2:
                    points.print_list(point)

                if chooise == 3:
                    point.info()

                    """
                    Här ska vara filmer som man väler för att få bonus laddat på kontot. Vi ska koppla den 
                    delen ihop med där man väljer filmer"""

                if chooise==4:
                    break
        if choise == 3:

           print("¤¤¤¤¤¤Snack Meny¤¤¤¤¤¤")
           print("1:Snack pris 20p")
           print("2:Dricka pris 20p")
           print("3:Combo pris 30p")
           print("4.Exit")

           val=int(input("Välj:"))
           if val==1:
              point.saldo=snack.snack
              points.add_saldo(point)
           elif val==2:
              point.saldo=drink.drink
              points.add_saldo(point)
           elif val==3:
              point.saldo=combo.snack
              point.saldo=combo.drink
              points.add_saldo(point)
              points.add_saldo(point)
           if choise == 4:
               break

        if choise == 5:
            break







if __name__ == "__main__":
    main()
