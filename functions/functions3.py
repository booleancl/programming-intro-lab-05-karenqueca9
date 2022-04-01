#Funciones con parametros
def print_param(daddy):
    print(daddy)
    print(daddy)

#No es necesario que el nombre del objeto que vamos a pasar como argumento sea el mismo que el nombre del parametro
print_param(77)

singer = "marcianeke"
print_param(singer)

#Volumen de una esfera que recibe un parametro que es el radio
#Formula 4/3 pi r3
def volume(radio):
  Result =   4/3 * 3.14 * radio **3
  print(Result)

big =  7
small = 2
volume(big)
volume(small)

def multiply_by_2(number):
    number = number * 2
    print(number)

multiply_by_2(big)
print(big)    

#funcion de dos parametros

def concat_strings(strl,str2):
    longstr = strl + " " + str2
    print(longstr)

text1 = "pasito a pasito"
text2 = "suave suavecito"
concat_strings(text1,text2)    
