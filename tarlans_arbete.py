class Person:

    def __init__(self, firstname,lastname,personalnumber):
        self.firstname=firstname
        self.lastname=lastname
        self.personalnumber=personalnumber

    def print_name(self):
        print(self.firstname, self.lastname, self.personalnumber)



def main():
    List_of_all_members = []
    while True:
           print("___________Menyval__________")
           print("Tryck 1 för att spara personuppgifter")
           print("Tryck 2 för att visa sparade personuppgifter")
           Val=input("Val:")
           Val=int(Val)


           if Val==1:
               firstname=input("Skriv in dit Förnamn")
               Inmatning_firstname = Person(firstname,None,None)
               Inmatning_firstname.print_name()
               List_of_all_members.append(firstname)

               lastname=input("Skriv in dit efternamn")
               Inmatning_lastname = Person(lastname, firstname,None)
               Inmatning_lastname.print_name()
               List_of_all_members.append(lastname)

               personalnumber=input("Skriv in din personnumber")
               personalnumber=int(personalnumber)
               personalnumber = Person(personalnumber,firstname,lastname)
               personalnumber.print_name()
               List_of_all_members.append(personalnumber)


           if Val==2:
               print(List_of_all_members)





if __name__ == "__main__":
    main()