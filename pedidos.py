#lasanha R$ 8,00
#estrogonofe R$ 11,00

#suco R$ 2,50
#refrigerante R$ 3,00
comida = input()
bebida = input()

def calc(comida, bebida):
    comida= comida.lower()
    bebida= bebida.lower()
    valor=0

    if comida == "lasanha":
                valor+=8.00
    elif comida =="estrogonofe":
                valor +=11.00
    if bebida == "refrigerante":
                valor += 3.00
    elif bebida =="suco":
                valor+= 2.50
    print ("{:.2f}".format(valor))
    return valor
calc(comida, bebida)
    
