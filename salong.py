class Salong:
    def __init__(self, name, points, seats):
        self.name = name
        self.points = points
        self.seats = seats


    def introduce_self(self):
        print("Salongen är " + self.name)
        print("Det kostar totalt " + self.points)
        print("Det finns totalt", self.seats, "platser")

# s1 = Salong("Svea", "140 poäng", 200)
# s2 = Salong("Thor", "100 poäng", 150)
# s3 = Salong("Greta", "80 poäng", 100)
#
# s1.introduce_self()
# s2.introduce_self()
# s3.introduce_self()


class Film:
    def __init__(self, name= "", genre="", information=""):
        self.name = name
        self.genre = genre
        self.information = information

    def __str__(self):
        return f"{self.name} i genre {self.genre}\n{self.information}"

class Filmer:
    def __init__(self):
        self.List_of_all_movies = []

# Läs in samtliga filmer från en fil, skapa ett filmobjekt för varje och lagra i List_of_all_movies

        with open('SamtligaFilmer.txt', 'r') as f:
            for i in range(3):
                 = line.split(";")
                l1 = f.readline()
                l2 = f.readline()
                film_name = ""
                film_genre = ""
                film_info = ""
                filmen = Film(film_name, film_genre, film_info)
                self.List_of_all_movies.append(filmen)


                #best_round = [0, 0, 0]
                #for line in open("rounds.txt", "r"):
                #   data = line.split(";")
                #data[2] = int(data[2])
                #if best_round[2] == 0 or data[2] < best_round[2]:
                #    best_round = data
                #print("Best round is:")
                #print(f"{best_round[0]}, {best_round[1]} {best_round[2]}")




    def add_movie(self, movie):
        self.List_of_all_movies.append(movie)

    def print_movie(self):
        return print(self.movie, self.genre, self.information)

    def __repr__(self):
        return str(self.movie) + "." + str(self.genre) + "." + str(self.information)

    def print_list(self):
        return print(self.List_of_all_movies)


class Menu:
    def __init__(self):
        self.movies = filmer()

    def show_menu(self):
        while True:
            try:
                print("___________Menyval__________")
                print("Tryck 1 för att visa filmen Sound of music")
                print("Tryck 2 för att visa filmen Terminator")
                print("Tryck 3 för att visa filmen Smurfarna")
                print("Tryck 4 för att lägga till film")
                print("Tryck 5 för att visa alla filmer")
                Val = input("Val:")
                Val = int(Val)
            except ValueError:
                print("Välj endast mellan 1 eller 3!")

            if Val == 4:
                movie = Film()
                movie.name = input("Ange filems titel: ")
                movie.genre = input("Ange filems genre: ")
                movie.information = input("Ange filems information: ")

                self.movies.add_movie(movie)

            if Val == 5:
                for movie in self.movies.List_of_all_movies:
                    print(movie)


# dunderinit
            # if Val == 1:
            #     movie = input("Välj film")
            #     Inmatning_movie = filmer.movie(movie, None, None)
            #     List_of_all_movies.append(movie)
            #     genre = input("Välj genre")
            #     Inmatning_genre = filmer.genre(movie, genre, None)
            #     List_of_all_movies.append(genre)
            #     information = input("Vill du se information om filmen?")
            #     Inmatning_information = filmer.information(movie, genre, information)
            #     List_of_all_movies.append(information)
            # if Val == 2:
            #     genre = input("Välj genre")
            #     genre = int(genre)
            #     genre = filmer.genre(movies, genre, information)
            #     List_of_all_movies.append(information)
            #     genre.print_movie()
            # if Val == 3:
            #     information = input("Vill du se information om filmen?")
            #     information = int(information)
            #     information = filmer.information(movie, genre, information)
            #     List_of_all_movies.append(information)
            #     information.print_movie()
            #
            #
            #     except ValueError:
            #         print("Endast siffror!")


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == "__main__":
    main