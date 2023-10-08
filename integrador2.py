
from readchar import readkey,key # de esta manera importas solo esas dos que es lo que necesitas
input_str = ""
while True:
    leido = readkey() # Se ingresara la tecla a presionar
    print("leer tecla", leido)
    (input_str) += leido
    if leido == key.UP: # acá le das la instrucción de que al precionar la tecla arriba que es lo que va realizar
        break
        

