class Menu:
    def __init__(self):
        self.choices = {
            "1": self.new_account,
            "2": self.book,
            "3": self.kiosk,

        }

    def new_account(self):
        print("tjabbatjena")

    def book(self):
        print("tjenatjena")

    def kiosk(self):
        print("tjabbatjenahallå")

    def

    def menu_print1(self):
        print("""
                 Notebook Menu 
                   1. Skapa nytt konto
                   2. Boka biljett
                   3. Handla i kiosken
                   4. Kolla aktuella filmer""")

    def run_menu(self):
        while True:
            self.menu_print1()
            choice = input("Ange ditt val: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("felaktig inmatning")


"""def main_menu():
    while True:
        valid_numbers = [1, 2, 3, 4, 5]
        print("")
        print("*" * 25)
        print("1. Skapa nytt konto:")
        print("2. Boka Biljett:")
        print("3. Handla i kiosken:")
        print("4. Kolla aktuella filmer")
        print("5. Avsluta programmet:")
        print("*" * 25)
        choise = int(input("Ange ditt val: "))
        print("*" * 25)
        if choise in valid_numbers:
            if choise == 1:
                pass
            if choise == 2:
                pass
            if choise == 3:
                pass
            if choise == 4:
                pass
            if choise == 5:
                break"""


def main():
    a = Menu()
    a.run_menu()


if __name__ == '__main__':
    main()
