class Saldo_Menu:
    def __init__(self,saldo=0, spenderade_point=0,bonus=0):
        self.saldo=saldo
        self.spenderade_point=spenderade_point
        self.bonus=bonus

    def __str__(self):
        return f"{self.saldo}, {self.spenderade_point}, {self.bonus}"

    def __repr__(self):
        return f"{self.saldo}, {self.spenderade_point}, {self.bonus}"


    def info (self):
        if self.saldo == 0:
            print("Tyvär du har inte tillräcklig med poäng!" + "--" + str(self.saldo) + "Kr")
            return self.saldo
        if self.spenderade_point == 0:
            return str(self.saldo)
        else:
            print(str(self.saldo) + "Kr har sparats")


class Point:

    def __init__(self):
        self.list_saldo = []

    def add_saldo(self,point):
        self.list_saldo.append(point)

    def print_saldo(self, spenderade_point,saldo):
        print(str(sum([value.saldo for value in self.list_saldo]) - spenderade_point) + "Kr har kvar i kontot")
        if spenderade_point>saldo:
            print("Tyvärr går ej handla mer än det som du har!")


    def print_list(self,point):
        for i in self.list_saldo:
           if i ==point:
               print(i.spenderade_point,"Poäng har du spenderat")


def main():

    points=Point()
    point=Saldo_Menu()

    print("___________MENU____________")
    print("1.Visa saldo")
    print("2.Spendering av poäng")
    print("3.Plånboken")

    while True:
        try:
            Chooise=input("Välj:__")
            Chooise=int(Chooise)
        except ValueError:
            print("Välj endast 1 eller 2!")
        if  Chooise==1:
            try:
                point=Saldo_Menu()
                point.saldo=int(input("Skriv in din intjänade bonus:"))
                point.spenderade_point=int(input("Skriv in dina spenderade poäng?:"))
                points.add_saldo(point)
                points.print_saldo(point.spenderade_point,point.saldo)

            except ValueError:
                print("Summan i sifror endast!")
        if Chooise==2:

            points.print_list(point)

        if Chooise==3:

            point.info()



            """
            Här ska vara filmer som man väler för att få bonus laddat på kontot. Vi ska koppla den 
            delen ihop med där man väljer filmer"""





if __name__ == "__main__":
    main()