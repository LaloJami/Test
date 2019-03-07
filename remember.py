
#hola mundo
print("hola mundo")
#declarar variables
myinteger=10        #integer
mystring="casa"   #string
myfloat=3.5      #flat
mystring2= "se pueden escribir una cadena de caracteres"
letra=mystring[1]   #se puede capturar la letra de una cadena(string) esta se cuenta desde el 0
sumacaracter=mystring+ " " +mystring2 #se pueden sumarr dos strings 
sumaint=myinteger+myfloat   #se puede sumar entre un integer y un float sin embargo la variable resultante sera un float
sumaintchar=myinteger+mystring #no se puede sumar strings con integers o floats

print(mystring2[2:7]) #>>pued  me da una parte de la cadena original, en particular desde la 2 hasta la 7
print(mystring2[:7])  #se pued me da una parte de la cadena original desde el inicio hasta la posicion 7
print(mystring2[30:]) #de caracteres, me da una parte de la cadena original desde la posicion original hasta el final
print(len(mystring)) #funcion len() te permite saber el numero de caracteres que tiene un string 
print(mystring[-2]) #cuenta los caracteres desde atras

##podemos comparar cadenas pero no podemos modificarlas!!!
##para modificar uuna cadena, es mejor crear otra con el nuevo mensaje adicional y hacer una suma de cadenas

##OPERADOR IN
#"c" in mystring #>>True 

#crear una funcion 
def elimina_vocales(s):     #funcion que acepta un parametro s
    vocales = "aeiouAEIOU"  #se inicializa una variable donde se deja todas las vocales
    s_sin_vocales = ""      #se inicializa una variable vacia
    for letra in s:         #por cada letra en s hacer
        if letra not in vocales:    #comparo si letra no esta en vocales entonces
            s_sin_vocales += letra  #s_sin_vocales se le agrega la letra actual
    return s_sin_vocales    #al final del for se retorna la variable s_sin_vocales

elimina_vocales(mystring)


##NOTA: PARA WHILE Y FOR NO NECESITAN DE LLAVES SIN EMBARGO LOS TABS SON IMPORTANTES
##programa while,
fruta="banana"
indice=0
while indice < len(fruta):  #mientras el indice sea menor que la longitud de la variable fruta hacer:
    letra = fruta[indice]   #letra toma el caracter numero (indice) de fruta
    print(letra)            #se imprime letra
    indice +=1              #se le suma uno al indice
#cuando indice es mayor a la longitud de fruta el programa se detiene

##programa for,
for caracter in fruta:      #por cada caracter(se define la variable caracter la cual sera un elemento) en fruta
    print(caracter)         #imprimir caracter
    
