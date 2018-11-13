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

    def input_person_info(self):
        self.first = input("Skriv in ditt förnamn:")
        self.last = input("Skriv in ditt efternamn:")
        self.persno = input("Skriv in ditt personnr:")
        return self



class Person_collection:
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



class Menus:
    def __init__(self):
        self.salong1 = Salon("Svea", 200, 140)
        self.salong2 = Salon("Thor", 150, 100)
        self.salong3 = Salon("Greta", 100, 80)
        self.person = Person()
        self.persons = Person_collection()
        self.saldo = Saldo_Menu()
        self.points = Point()



    def print_new_user_menu(self):
        print("Huvudmeny:")
        print("Tryck 1 för att spara personuppgifter")
        print("Tryck 2 för att visa sparade personuppgifter")
        print("Tryck 3 för att gå till huvudmenyn!")

    def run_new_user_menu(self):
        self.print_new_user_menu()
        choice = input("Ange ditt val: ")
        choice = int(choice)
        if choice == 1:
            self.person.input_person_info()
        if choice == 2:
            self.persons.print_list()
        if choice == 3:
            self.print_main_menu()
            self.run_main_menu()
        else:
            print("felaktig inmatning")

    def print_main_menu(self):
        print("1. Saldokollen")
        print("2. Handla i kiosk")
        print("3. Kolla aktuella filmer")
        print("4. Avsluta programmet")
        print("*" * 25)


    def run_main_menu(self):
        self.print_main_menu()
        choice = input("Ange ditt val: ")
        choice = int(choice)
        if choice == 1:
            self.run_saldo_menu()
        if choice == 2:
            pass
        if choice == 3:
            pass
        else:
            print("felaktig inmatning")

    def print_saldo_menu(self):
        print("Saldomeny:")
        print("1.Aktuellt saldo")
        print("2.Spenderade poäng")
        print("3.Plånboken")
        print("4.Kontoladning")
        print("5.Exit")


    def run_saldo_menu(self):
        self.print_saldo_menu()
        choice = input("Ange ditt val: ")
        choice = int(choice)
        if choice == 1:
            self.points.print_saldo(self.saldo.spenderade_point, self.saldo.saldo)
        if choice == 2:
            self.points.print_list(self.saldo)
        if choice == 3:
            pass
        else:
            print("felaktig inmatning")


    def print_kiosk_menu(self):
        print("Snack Meny")
        print("1:Snack pris 20p")
        print("2:Dricka pris 20p")
        print("3:Combo pris 30p")
        print("4.Exit")

    def run_kiosk_menu(self):
        pass

    def print_booking_menu(self):
        print("*" * 50)
        print(f"1: Sound Of Music")
        print(f"2: Ragnarök")
        print(f"3: Surviving Summer")
        print(f"4: Boka film")
        print("*" * 50)

    def run_booking_menu(self):

        print("1. 100p =100kr")
        print("2. 150p =150kr")
        print("3. 500p =500kr")
        print("4. 1000p =1000kr")
        print("5. Exit")
        print("Välj summan som du vill ladda!")


def main():
    a = Menus()
    a.run_new_user_menu()

if __name__ == "__main__":

    main()