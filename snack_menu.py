class Drink_menu:
    def __init__(self, drink):
        self.drink = drink
        self.p = 20

    def __str__(self):
        return f"{self.drink}, {self.p} points"

    def __repr__(self):
        return f"{self.drink}, {self.p} points"


class Snack_menu:
    def __init__(self, snack):
        self.snack = snack
        self.p = 20

    def __str__(self):
        return f"{self.snack}, {self.p} points"

    def __repr__(self):
        return f"{self.snack}, {self.p} points"


class Combo_menu(Drink_menu, Snack_menu):
    def __init__(self, drink, snack):
        Drink_menu.__init__(self, drink)
        Snack_menu.__init__(self, snack)
        self.p = 30

    def __str__(self):
        return f"{self.snack}, {self.drink}, {self.p} points"

    def __repr__(self):
        return f"{self.snack}, {self.drink}, {self.p} points"


class Menus:
    def __init__(self):

        menu1 = Drink_menu("Coke")
        menu2 = Snack_menu("Popcorn")
        menu3 = Combo_menu("Popcorn", "Coke")

        self.menues = [menu1, menu2, menu3]

    def print_menus(self):
        for i, menu in enumerate(self.menues):
            print("Meny", i + 1, menu)

    def kioskmenu(self):
        self.choices = {
            "1": self.menues

    def menu_print1(self):
        print("""
                 Filmstaden
                   1. Prislista""")

    def run_menu(self):
        while True:
            self.menu_print1()
            choice = input("Ange ditt val: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("felaktig inmatning")


def main():
    a = Menus()
    a.run_menu()


    #menus = Menus()
    #menus.print_menus()


if __name__ == '__main__':
    main()
