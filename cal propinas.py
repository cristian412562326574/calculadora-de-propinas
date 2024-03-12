class Cal_propinas():
    cuenta = 0.0
    propina_dada = 0.0
    propina_fija = 5

    def calcular (self):
        self.resultado = ( self.cuenta  / 100 ) * self.propina_dada

    def calcular_propina_fija(self):
        self.resultado = ( self.cuenta * self.propina_fija) / 100

    def suma(self , opcion):
        if opcion == "S":
            self.resultado = self.resultado + self.cuenta
        else:
            self.resultado = self.resultado + self.cuenta

propina = Cal_propinas()
opcion = str.upper(input( " Por politicas del restaurante se deja una propina del 5% deseas dejar otro monto si(S) O no(N)"))
if opcion ==  "S":
    propina.cuenta=float(input("Ingrese el monto de la cuenta: "))
    propina.propina_dada=float(input("Ingrese la cantidad de dinero que se le da como propina: "))
    propina.calcular()
    print("Tienes que dar de propina la cantidad de : " , propina.resultado)
    opcion = str.upper(input(" Quieres saber el total de dinero que quieres dar ? S(si) o N(no)"))
    if opcion == "S":
        propina.suma(opcion)
        print(" Para una cantidad de :" ,  propina.resultado)
    else:
        pass
elif opcion == "N":
    propina.cuenta=float(input("Ingrese el monto de la cuenta: "))
    propina.calcular_propina_fija()
    print("Tienes que dar de propina la cantidad de : " , propina.resultado)
    opcion = str.upper(input(" Quieres saber el total de dinero que quieres dar ? S(si) o N(no)"))
    if opcion == "S":
        propina.suma(opcion)
        print(" Para una cantidad de :" ,  propina.resultado)
    else:
        pass
else:
    print ("Opcion no valida")