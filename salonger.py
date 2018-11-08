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






def main():
    movie_info_one = Salons()
    print(movie_info_one.salon1)
    print(movie_info_one.salon1.points)


if __name__ == '__main__':
    main()


    """movie_info = Movie_info()
    print(movie_info.thor)
    salon_info = Salons()
    salon_info.print_movies()
    movie_info_one = Salons()
    print(movie_info_one.salon1)
    print(movie_info_one.salon2)
    print(movie_info_one.salon3)
    print(movie_info_one.salon1.points)
    print(movie_info_one.salon2.points + movie_info_one.salon1.points)"""