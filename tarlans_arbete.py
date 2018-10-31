class Person:

    def __init__(self, firstname,lastname,personalnumber):
        self.List_of_all_members=[]
        self.firstname=firstname
        self.List_of_all_members.append(firstname)
        self.lastname=lastname
        self.List_of_all_members.append(lastname)
        self.personalnumber=personalnumber
        self.List_of_all_members.append(personalnumber)

    def print_name(self):
        return print(self.firstname, self.lastname, self.personalnumber)

    def __repr__(self):
        return str(self.firstname) + "." + str(self.lastname) + "." + str(self.personalnumber)

    def print_list(self):
        return print(self.List_of_all_members)


def main():
    List_of_all_members = []
    while True:
           try:
               print("___________Menyval__________")
               print("Tryck 1 för att spara personuppgifter")
               print("Tryck 2 för att visa sparade personuppgifter")
               Val=input("Val:")
               Val=int(Val)
           except ValueError:
               print("Välj endast mellan 1 eller 2!")


           if Val==1:
               firstname=input("Skriv in dit Förnamn")
               Inmatning_firstname = Person(firstname,None,None)
               List_of_all_members.append(firstname)
               lastname=input("Skriv in dit efternamn")
               Inmatning_lastname = Person(firstname,lastname,None)
               List_of_all_members.append(lastname)
               try:
                   personalnumber=input("Skriv in din personnumber")
                   personalnumber=int(personalnumber)
                   personalnumber = Person(firstname,lastname,personalnumber)
                   List_of_all_members.append(personalnumber)
                   personalnumber.print_name()
               except ValueError:
                   print("Endast siffror!")

           if Val==2:
               str1 = "".join(map(str, List_of_all_members))
               print(str1)





if __name__ == "__main__":
    main()