import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("BIO")

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
            print("Tyvär du har inte tillräcklig med poäng!" + "--" + str(self.saldo))
            return self.saldo
        else:
            print(str(self.saldo) + "Poäng har sparats")

class Point:

    def __init__(self):
        self.list_saldo = []

    def add_saldo(self,point):
        self.list_saldo.append(point)


    def print_saldo(self, spenderade_point,saldo):
        if spenderade_point>=0:
            print(str(sum(([value.saldo for value in self.list_saldo]+[value.bonus for value in self.list_saldo])) - spenderade_point)+" " + "Poäng kvar på kontot")
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

class Combo_menu:
   def __init__(self, combo=30):
       self.combo = combo
   def __str__(self):
       return f"{self.combo}, {self.p} points"

   def __repr__(self):
       return f"{self.combo}, {self.p} points"


class Menus:
    def __init__(self):
        self.person = Person()
        self.persons = Person_collection()
        self.saldo = Saldo_Menu()
        self.points = Point()
        self.snack = Snack_menu()
        self.drink = Drink_menu()
        self.combo = Combo_menu()
        self.movie_info = Movie_info()

        self.salong1 = Salon("Svea", 200, 140)
        self.salong2 = Salon("Thor", 150, 100)
        self.salong3 = Salon("Greta", 100, 80)
    def print_new_user_menu(self):
        print("Huvudmeny:")
        print("Tryck 1 för att spara personuppgifter")
        print("Tryck 2 för att visa sparade personuppgifter")
        print("Tryck 3 för att gå till huvudmenyn!")
        print("*" * 25)


    def run_new_user_menu(self):
        while True:
            self.print_new_user_menu()
            try:
                choice = input("Ange ditt val: ")
                choice = int(choice)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
            if choice == 1:
                self.first = input("Skriv in ditt förnamn:")
                self.last = input("Skriv in ditt efternamn:")
                self.persno = input("Skriv in ditt personnr:")
                with open("Personregister.txt", "a")as f:
                    f.write(f"{self.first};{self.last};{self.persno}\n")
                self.persons.add_person(self.first)
                self.persons.add_person(self.last)
                self.persons.add_person(self.persno)
            elif choice == 2:
                self.persons.print_list()
            elif choice == 3:
                i = input("Skriv din personnummer!:")
                numbers = [line.split(';')[2].rstrip() for line in open('Personregister.txt', 'r')]
                if i in numbers:
                    tkinter.messagebox.showinfo("BIOGRAFEN MEDDELAR", "VÄLKOMMEN KÄRA KUND!")
                    response = tkinter.messagebox.askquestion("BIOGRAFEN", "ÄR DU NY KUND?")
                    if response == 1:
                        tkinter.Label(window, text="---VÄLKOMMEN HOPPAS DU BLIR NÖJD IDAG---",
                                      font=("Arial Bold", 20)).pack()
                        tkinter.Label(window, text="STÄNG NER FÖR ATT GÅ VIDARE!", font=("Arial", 10)).pack()
                    else:
                        tkinter.Label(window, text="---VÄLKOMMEN HOPPAS DU BLIR NÖJD IDAG---", font=("Arial Bold", 20)).pack()
                        tkinter.Label(window, text="STÄNG NER FÖR ATT GÅ VIDARE!",font=("Arial", 10)).pack()

                    window.mainloop()
                    self.run_main_menu()
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

    def print_main_menu(self):
        print("1. Saldokollen")
        print("2. Handla i kiosk")
        print("3. Kolla aktuella filmer")
        print("4. Avsluta programmet")
        print("*" * 25)


    def run_main_menu(self):
        while True:
            self.print_main_menu()
            try:
                choice = input("Ange ditt val: ")
                choice = int(choice)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
            if choice == 1:
                self.run_saldo_menu()
            if choice == 2:
                self.run_kiosk_menu()
            if choice == 3:
                self.run_booking_menu()
            elif choice==4:
              exit(self.run_new_user_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

    def print_saldo_menu(self):
        print("Saldomeny:")
        print("1.Aktuellt saldo")
        print("2.Spenderade poäng")
        print("3.Plånboken")
        print("4.Kontoladning")
        print("5.Exit")
        print("*" * 25)

    def run_saldo_menu(self):
        while True:
            self.print_saldo_menu()
            try:
                choice = input("Ange ditt val: ")
                choice = int(choice)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
            if choice == 1:
                self.points.print_saldo(self.saldo.spenderade_point, self.saldo.saldo)
            elif choice == 2:
                self.points.print_list(self.saldo)
            elif choice == 3:
                self.saldo.info()
            elif choice==4:
                self.run_kontolad_menu()
            elif choice==5:
                exit(self.run_main_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

    def print_kiosk_menu(self):
        print("Snack Meny")
        print("1:Snack pris 20p")
        print("2:Dricka pris 20p")
        print("3:Combo pris 30p")
        print("4.Exit")
        print("*" * 25)

    def run_kiosk_menu(self):
        while True:
            self.print_kiosk_menu()
            try:
                Chooise=input("Välj en av alternativen!")
                Chooise=int(Chooise)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
            if Chooise==1:
                self.saldo.spenderade_point = self.snack.snack
                self.points.add_saldo(self.saldo)
            elif Chooise==2:
                self.saldo.spenderade_point = self.drink.drink
                self.points.add_saldo(self.saldo)
            elif Chooise==3:
                self.saldo.spenderade_point = self.combo.combo
                self.points.add_saldo(self.saldo)
            elif Chooise==4:
                exit(self.run_main_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
    def print_booking_menu(self):
        print("*" * 50)
        print(f"1: Sound Of Music")
        print(f"2: Ragnarök")
        print(f"3: Surviving Summer")
        print(f"4: Boka film")
        print(f"5: Exit")
        print("*" * 50)

    def run_booking_menu(self):
        while True:
            self.print_booking_menu()
            try:
                Chooise=input("Välj en av alternativ!")
                Chooise=int(Chooise)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

            if Chooise==1:
                print("*" * 19)
                print(self.movie_info.format_movie(self.movie_info.movie_svea()))
                print("*" * 111)
            elif Chooise==2:
                print("*" * 14)
                print(self.movie_info.format_movie(self.movie_info.movie_thor()))
                print("*" * 119)
            elif Chooise==3:
                print("*" * 21)
                print(self.movie_info.format_movie(self.movie_info.movie_greta()))
                print("*" * 94)
            elif Chooise ==4:
                self.run_film_meny()

            elif Chooise ==5:
                exit(self.run_main_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
    def print_film_meny(self):
        print("*" * 50)
        print(f"1: {self.salong1} och visar filmen Sound Of Music")
        print(f"2: {self.salong2} och visar filmen Ragnarök")
        print(f"3: {self.salong3} och visar filmen Surviving Summer")
        print(f"4: Exit")
        print("*" * 50)

    def run_film_meny(self):
        while True:
            self.print_film_meny()
            try:
                val4 = input("Välj vilken film du vill boka")
                val4 = int(val4)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue
            if val4 == 1:
                print("*" * 10)
                print("Du har bokat filmen Sound Of Music")
                print(f"Som visas i salong {self.salong1.namn} och kostar {self.salong1.pris} Poäng")
                bonus = 10
                self.saldo.bonus = bonus
                self.saldo.spenderade_point = self.salong1.pris
                self.points.add_saldo(self.saldo)
                print("*" * 10)
            elif val4 == 2:
                print("*" * 10)
                print("Du har bokat filmen Ragnarök")
                print(f"Som visas i salong {self.salong2.namn} och kostar {self.salong2.pris} Poäng")
                bonus = 10
                self.saldo.bonus = bonus
                self.saldo.spenderade_point = self.salong2.pris
                self.points.add_saldo(self.saldo)
                print("*" * 10)
            elif val4 == 3:
                print("*" * 10)
                print("Du har bokat filmen Surviving Summer")
                print(f"Som visas i salong {self.salong3.namn} och kostar {self.salong3.pris} Poäng")
                bonus = 10
                self.saldo.bonus = bonus
                self.saldo.spenderade_point = self.salong3.pris
                self.points.add_saldo(self.saldo)
                print("*" * 10)
            elif val4==4:
                exit(self.run_booking_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue



    def print_kontolad_menu(self):
        print("1. 100p =100kr")
        print("2. 150p =150kr")
        print("3. 500p =500kr")
        print("4. 1000p =1000kr")
        print("5. Exit")
        print("Välj summan som du vill ladda!")
        print("*" * 25)

    def run_kontolad_menu(self):
        while True:
            self.print_kontolad_menu()
            try:
                Chooise=input("Välj en av alternativ!")
                Chooise=int(Chooise)
                print("*" * 25)
            except ValueError:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

            if Chooise==1:
                self.points.add_saldo(Saldo_Menu(100))
            elif Chooise==2:
                self.points.add_saldo(Saldo_Menu(150))
            elif Chooise==3:
                self.points.add_saldo(Saldo_Menu(500))
            elif Chooise==4:
                self.points.add_saldo(Saldo_Menu(1000))
            elif Chooise==5:
                exit(self.run_saldo_menu())
            else:
                print("Tryck OK för att fortsätta!")
                tkinter.messagebox.showinfo("-------------!!!!!OBS!!!!!!----------", "FELAKTIG INMATNING!!!")
                continue

def main():

    a = Menus()
    a.run_new_user_menu()

if __name__ == "__main__":
    main()
