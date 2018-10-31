class Poäng:

    def __init__(self,saldo,spenderade_point,bonus):
        self.List_Saldo=[]
        self.saldo=saldo
        self.List_Saldo.append(saldo)
        self.spenderade_point=spenderade_point
        self.bonus=bonus

    def print_saldo(self):
        for i in self.List_Saldo:
          saldot=i-self.spenderade_point
          return print(str(saldot)+"Kr har kvar i kontot")
    def __repr__(self):
        if self.saldo==0:
            print("Tyvär du har inte tillräcklig med poäng!"+ "--"+ str(self.saldo)+"Kr")
            return self.saldo
        if self.spenderade_point == 0:
            return str(self.saldo)
        else:
            text = "".join(map(str, self.List_Saldo))
            print(text+"Kr har sparats")
            return self.saldo






def main():

    print("___________MENU____________")
    print("1.Visa saldo")
    print("2.Bonus")

    while True:
        try:
            Chooise=input("Välj:__")
            Chooise=int(Chooise)
        except ValueError:
            print("Välj endast 1 eller 2!")
        if Chooise==1:
            try:
                Saldo=input("Skriv in din intjänade bonus--")
                Saldo=int(Saldo)
                Spenderade_points=input("Skriv in dina spenderade poäng?:")
                Spenderade_points=int(Spenderade_points)
                Saldo = Poäng(Saldo, Spenderade_points, None)
                Spenderade_points=Poäng(Saldo,Spenderade_points,None)
                Saldo.print_saldo()
            except ValueError:
                print("Summan i sifror endast!")
        if Chooise==2:
            """
            Här ska vara filmer som man väler för att få bonus laddat på kontot. Vi ska koppla den 
            delen ihop med där man väljer filmer"""





if __name__ == "__main__":
    main()