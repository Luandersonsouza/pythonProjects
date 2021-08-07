#lasanha R$ 8,00, estrogonofe R$ 11,00, suco R$2,50 e refrigerante R$ 3,00
import time

print("Ola, sou Diana a sua atendente virtual.")
time.sleep(3)
print("No nosso cardapio temos :")
print("Lasanha -> 8,00            Estrogonofe -> 11,00")
print("Refrigerante -> 3,00       Suco -> 2,50")
time.sleep(2)
print("Hoje voce ira saborear qual delicia do nosso cardapio?")
comida = input()
time.sleep(1)
print("E para quantas pessoas voce vai pedir?")
contc= int(input())
time.sleep(1)
print("Qual bebida?")
bebida = input()
time.sleep(1)
print("E para quantas pessoas voce vai pedir?")
contb= int(input())
time.sleep(2)
print("Pedido sendo preparado")
time.sleep(10)

def calc(comida, bebida):
    comida= comida.lower()
    bebida= bebida.lower()
    valor=0  
    
    if comida == "lasanha":
                valor+=8.00 * contc
    elif comida =="estrogonofe":
                valor +=11.00 * contc
    if bebida == "refrigerante":
                valor += 3.00 * contb
    elif bebida =="suco":
                valor+= 2.50 * contb
    print ("Total a ser pago : R${:.2f}".format(valor))
    time.sleep(3)
    print("Bom apetite!")
    return valor
calc(comida, bebida)