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


def main():

    persons = Person_Collection()

    while True:
        try:
            print("___________Menyval__________")
            print("Tryck 1 för att spara personuppgifter")
            print("Tryck 2 för att visa sparade personuppgifter")
            Val = input("Val:")
            Val = int(Val)
        except ValueError:
            print("Välj endast mellan 1 eller 2!")

        if Val == 1:
            person = Person()
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

            person_list_unik = [0, 0, 0]
            for line in open("Personregister.txt", "r"):
                data = line.split(";")
            data[2] = int(data[2])
            if person_list_unik[2] == person.personalnumber:
                person_list_unik = data
            print("Personnumret finns redan registrerad!")


        if Val == 2:
            persons.print_list()


if __name__ == "__main__":
    main()