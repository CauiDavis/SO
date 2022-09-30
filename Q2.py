import threading
import time        
x=0
Ca = False
Cb = False
lista=[]
def processo_0():
  global Ca,Cb
  for i in range(3):
    while Cb == True:
      print("ESPERA OCUPADA DE 00 POIS X=",x)
      time.sleep(2)
    
    Ca = True
    print("Entrando na RC de 00...")
    tamanho=len(lista)
    #time.sleep(5)
    lista.insert(tamanho,f'Item_{tamanho}')
    print("Saindo da RC de 00...")
    Ca = False
    
    print('Entrando na R. NÃO C. 00')
def processo_1():
  global Ca,Cb
  for i in range(3):
    while Ca == True:
      print("ESPERA OCUPADA DE 01 POIS X=",x)
      time.sleep(2)
    
    Cb = True
    print("Entrando na RC de 01...")
    tamanho=len(lista)
    lista.insert(tamanho,f'Item_{tamanho}')
    print("Saindo da RC de 01")
    Cb = False
    
    for j in range(5):
      print('Entrando na R. NÃO C. 01')
      time.sleep(5)

print("INICIO")
threading.Thread(target = processo_0).start()
threading.Thread(target = processo_1).start()
print("Final")