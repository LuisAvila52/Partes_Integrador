import os
import readchar

def clear_terminal(number):
    os.system('cls' if os.name == 'nt' else 'clear')
    if number == 50:
               print("aumentara contador hasta finalizar programa")
 
    else:
               print(f'Número actual: {number}')
        
number = 0
while number <= 50:
       
     
    key = readchar.readkey()
         
    if key =='n':
        clear_terminal(number)
        number +=1