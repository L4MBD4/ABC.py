#Calculadora basica
print ('Que operacion desea realizar :\n 1.SUMA \n 2.RESTA \n 3.MULTIPLICACION \n 4.DIVISION \n 5.MODULO')
Numero = int(input())
if Numero==1:
  print('Ingrese el primer numero :')
  Numero1= int(input())
  print('Ingrese el segundo numero :')
  Numero2= int(input())
  RSuma = Numero1 + Numero2
  print('El resultado es :',RSuma)
  
if Numero==2:
    print('Ingrese el primer numero :')
    Numero1= int(input())
    print('Ingrese el segundo numero :')
    Numero2= int(input())
    Rresta = Numero1 - Numero2
    print('El resultado es :',Rresta)
    
if Numero==3:
  print('Ingrese el primer numero :')
  Numero1= int(input())
  print('Ingrese el segundo numero :')
  Numero2= int(input())
  Rmulti = Numero1 * Numero2
  print('El resultado es :',Rmulti)

if Numero==4:
  print('Ingrese el primer numero :')
  Numero1= int(input())
  print('Ingrese el segundo numero :')
  Numero2= int(input())
  Rdiv = Numero1 / Numero2
  print('El resultado es :',Rdiv)
  
if Numero==5:
  print('Ingrese el primer numero :')
  Numero1= int(input())
  print('Ingrese el segundo numero :')
  Numero2= int(input())
  Rmod = Numero1 % Numero2
  print('El modulo es :',Rmod)