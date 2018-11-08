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


class Salon:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats

    def __str__(self):
        return f"{self.name} har {self.seats} platser och kostar {self.points} poäng"

class Salons:
    def __init__(self):
        self.salon1 = Salon(name="Svea", points=140, seats=200)
        self.salon2 = Salon(name="Thor", points=100, seats=150)
        self.salon3 = Salon(name="Greta", points=80, seats=100)
        self.salons = [self.salon1, self.salon2, self.salon3]

    def print_movies(self):
        for i, salon in enumerate(self.salons):
            print("Salong", i + 1, salon)


class Snack_menu:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __repr__(self):
        if self.snack1 == self.snack:
            return f"{self.name} kostar {self.points} poäng"
        if self.drink1 == self.drink:
            return f"{self.name} kostar {self.points} poäng"
        if self.combo1 == self.combo:
            return f"{self.snack.name} och {self.drink.name} kostar {self.combo.points} poäng"
        else:
            pass


class Snack_menus:

    def __init__(self):
        self.snack = Snack_menu(name="Snack", points=20)
        self.drink = Snack_menu(name="Coke", points=20)
        self.combo = (self.snack.name, self.drink.name, 30)
        self.all_menus = [self.snack, self.drink, self.combo]

    def print_kiosk_menu(self):
        for i, kiosk in enumerate(self.all_menus):
            print("Meny", i + 1, kiosk)


"""class Drink_menu:
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
       return f"{self.snack}, {self.drink}, {self.p} points"""



def main():
    while True:
        valid_numbers = [1, 2, 3]
        print("")
        print("*" * 25)
        print("1. drink")
        print("2. snack")
        print("3. combo")
        print("*" * 25)
        choise = int(input("Input Choice: "))
        print("*" * 25)
        if choise in valid_numbers:
            if choise == 1:
                print(Snack_menus)
            if choise == 2:
                pass
            if choise == 3:
                pass


    movie_info_one = Salons()
    print(movie_info_one.salon1)
    print(movie_info_one.salon1.points)
    min_meny = Snack_menus()
    print(min_meny.snack)

if __name__ == '__main__':
    main()
