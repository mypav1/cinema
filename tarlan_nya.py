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
        with open("svea.txt", "r", encoding="utf-8") as i:
            return i.readlines()


    def movie_thor(self):
        with open("thor.txt", "r", encoding="utf-8") as i:
            return i.readlines()

    def movie_greta(self):
        with open("greta.txt", "r", encoding="utf-8") as i:
            return i.readlines()


class Salon:

    def __init__(self, namn, seats, pris):
        self.namn = namn
        self.pris = pris
        self.seats = seats


    def __str__(self):
        return f"{self.namn} har {self.seats} platser och kostar {self.pris} poäng"






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

    def __init__(self,saldo=0,spenderade_point=0,bonus=0):
        self.saldo=saldo
        self.spenderade_point=spenderade_point
        self.bonus=bonus



    def __str__(self):
        return f"{self.saldo},{self.spenderade_point}, "


    def __repr__(self):
        return f"{self.saldo}, {self.spenderade_point}, "

    def info (self):

        if self.saldo == 0:
            print("Tyvär du har inte tillräcklig med poäng!" + "--" + str(self.saldo) + "Kr")
            return self.saldo
        else:
            print(str(self.saldo) + "Kr har sparats")



class Point:

    def __init__(self):
        self.list_saldo = []

    def add_saldo(self,point):
        self.list_saldo.append(point)


    def print_saldo(self, spenderade_point,saldo):
        if spenderade_point>=0:
            print(str(sum(([value.saldo for value in self.list_saldo]+[value.bonus for value in self.list_saldo])) - spenderade_point) + "Kr har kvar i kontot")
        elif spenderade_point>saldo:
            print("Tyvärr går ej handla mer än det som du har!")
        else:
            print("Saldot är tomt")

    def print_list(self,point):
        for i in self.list_saldo:
           if i ==point:
               print(i.spenderade_point,"Poäng har du spenderat!")



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

   def calc_combo(self):
       self.combo=self.snack+self.drink


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
    movie_info = Movie_info()
    salong1 = Salon("Svea", 200, 140)
    salong2 = Salon("Thor", 150, 100)
    salong3 = Salon("Greta", 100, 80)
    while True:
        print(" --Skapa nytt konto--")
        print("*" * 25)
        try:
            print("___________Menyval__________")
            print("Tryck 1 för att spara personuppgifter")
            print("Tryck 2 för att visa sparade personuppgifter")
            print("Tryck 3 för att gå till huvudmenun!")
            val1 = input("Val:")
            val1 = int(val1)
        except ValueError:
            print("Välj endast mellan 1 eller 3!")
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
            i=input("Skriv din personnummer!:")
            numbers = [line.split(';')[2].rstrip() for line in open('Personregister.txt', 'r')]
            if i in numbers:
                while True:
                    print("1. Saldokollen")
                    print("2. Handla i kiosk")
                    print("3. Kolla aktuella filmer")
                    print("4. Avsluta programmet")
                    print("*" * 25)
                    try:
                        choise = input("Ange ditt val: ")
                        choise=int(choise)
                    except ValueError:
                        print("Endast 1 till 4!")
                    print("*" * 25)
                    if choise == 1:
                        while True:
                            print("___________MENU____________")
                            print("1.Saldo")
                            print("2.Spendering av poäng")
                            print("3.Plånboken")
                            print("4.Kontoladning")
                            print("5.Exit")

                            try:
                                chooise = input("Välj:__")
                                chooise = int(chooise)
                            except ValueError:
                                print("Välj endast mellan 1 till 5!")
                            if chooise == 1:
                                points.print_saldo(point.spenderade_point, point.saldo)

                            elif chooise == 2:
                                points.print_list(point)
                            elif chooise == 3:
                                point.info()
                                """
                                Här ska vara filmer som man väler för att få bonus laddat på kontot. Vi ska koppla den 
                                delen ihop med där man väljer filmer"""
                            elif chooise==4:
                                while True:
                                    print("1. 100p =100kr")
                                    print("2. 150p =150kr")
                                    print("3. 500p =500kr")
                                    print("4. 1000p =1000kr")
                                    print("5. Exit")
                                    print("Välj summan som du vill ladda!")
                                    try:
                                        charge=input("Välj:")
                                        charge=int(charge)
                                    except ValueError:
                                        print("Välj endast mellan 1 till 5")


                                    if charge==1:
                                        points.add_saldo(Saldo_Menu(100))
                                    elif charge==2:
                                        points.add_saldo(Saldo_Menu(150))
                                    elif charge==3:
                                        points.add_saldo(Saldo_Menu(500))

                                    elif charge==4:
                                        points.add_saldo(Saldo_Menu(1000))

                                    elif charge==5:
                                        break


                            elif chooise==5:
                                break
                    if choise == 2:
                       print("¤¤¤¤¤¤Snack Meny¤¤¤¤¤¤")
                       print("1:Snack pris 20p")
                       print("2:Dricka pris 20p")
                       print("3:Combo pris 30p")
                       print("4.Exit")
                       val=int(input("Välj:"))
                       if val==1:

                          point.spenderade_point=snack.snack
                          points.add_saldo(point)
                       elif val==2:
                          point.spenderade_point=drink.drink
                          points.add_saldo(point)
                       elif val==3:

                          point.spenderade_point=combo.snack
                          point.spenderade_point=combo.drink
                          points.add_saldo(point)

                       elif val==4:
                           break

                    if choise == 3:
                        print("*" * 50)
                        print(f"1: Sound Of Music")
                        print(f"2: Ragnarök")
                        print(f"3: Surviving Summer")
                        print(f"4: Boka film")
                        print("*" * 50)
                        try:
                            val3 =input("Välj vilken film du vill läsa om:")
                            val3=int(val3)
                        except ValueError:
                            print("Välj endast mellan 1 till 4!")
                        if val3 == 1:
                            print("*" * 19)
                            print(movie_info.format_movie(movie_info.movie_svea()))
                            print("*" * 111)
                        elif val3 == 2:
                            print("*" * 14)
                            print(movie_info.format_movie(movie_info.movie_thor()))
                            print("*" * 119)
                        elif val3 == 3:
                            print("*" * 21)
                            print(movie_info.format_movie(movie_info.movie_greta()))
                            print("*" * 94)
                        elif val3 == 4:
                            print("*" * 50)
                            print(f"1: {salong1} och visar filmen Sound Of Music")
                            print(f"2: {salong2} och visar filmen Ragnarök")
                            print(f"3: {salong3} och visar filmen Surviving Summer")
                            print("*" * 50)
                            try:
                                val4 = input("Välj vilken film du vill boka")
                                val4=int(val4)
                            except ValueError:
                                print("Välj endast mellan 1 till 3!")
                            if val4 == 1:
                                print("*" * 10)
                                print("Du har bokat filmen Sound Of Music")
                                print(f"Som visas i salong {salong1.namn} och kostar {salong1.pris} Poäng")
                                bonus=10
                                point.bonus=bonus
                                point.spenderade_point = salong1.pris
                                points.add_saldo(point)
                                print("*" * 10)
                            elif val4 == 2:
                                print("*" * 10)
                                print("Du har bokat filmen Ragnarök")
                                print(f"Som visas i salong {salong2.namn} och kostar {salong2.pris} Poäng")
                                bonus = 10
                                point.bonus=bonus
                                point.spenderade_point = salong2.pris
                                points.add_saldo(point)
                                print("*" * 10)
                            elif val4 == 3:
                                print("*" * 10)
                                print("Du har bokat filmen Surviving Summer")
                                print(f"Som visas i salong {salong3.namn} och kostar {salong3.pris} Poäng")
                                bonus = 10
                                point.bonus=bonus
                                point.spenderade_point = salong3.pris
                                points.add_saldo(point)
                                print("*" * 10)
                    if choise == 5:
                        break


if __name__ == "__main__":

    main()