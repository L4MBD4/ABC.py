#IF
verdadero=False
if verdadero:
     print ("hola")
   
else:
      print ("Fuck!")
      
#RANGE?? genera numeros entre un rango
range (5)
list(range(5))#las enlista empezara desde 0

#For con un ejemplo de range
for var in list (range(5)):
   print (var)
   #For 
frutas = ['Sandia', 'Melon',  'Mango']
for Variable in range(len(frutas)):#Lent le los espacios que tenemos en frutas sin nesecidad de poner un numero exacto
   print ('Corriendo frutas :', frutas[Variable])
print ("Ready!")

''' Extras
tenemos  a
continue = que es para continuar
Break=Que hace lo de siempre
Pass=Lo salta segun la condicion
'''
#While
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Que no se cicle!")