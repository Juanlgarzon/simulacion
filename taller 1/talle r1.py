#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Generadores de numeros aleatorios: Congruencial mixto Y Cuadrados Medios
def periodo(lista):
    a=lista[1];
    ci=(lista.index(a, 2))-1;
    print("El periodo es= ",ci);
    
def mids(n,lista):
    x=float(input("Ingrese el valor de la semilla x0:\n "));
    i=0;
    while i < n:
        x=x*x;
        pu=(x//100)%10000;
        x=pu;
        u=round((pu/10000),5);
        lista.append(u);
        print(u);
        i=i+1;


    

def mtcar(n,lista):
    x=float(input("Ingrese el valor de la semilla x0: "));
    a=float(input("Ingrese el valor de a: "));
    c=float(input("Ingrese el valor de c: "));
    m=float(input("Ingrese el valor del modulo: "));
    i=0;
    print("Los numeros generados son: "); 
    while i < n:
    
        x=((a*x)+c)%m;
        u=x/m;           
        lista.append(u);   
        print(u);
        i=i+1;
    




lista=[];
print("Ingrese un numero para decidir cual generador de numeros pseudoaleatorios utilizar:\nGenerador congruencial mixto=1\nMetodo MidSquare=2\n");

gen=float(input());
n=float(input("Ingrese la cantidad maxima de numeros a generar: "));
if(gen==1):
    mtcar(n,lista);
    r=float(input("Desea conocer el periodo del generador creado?\nSi=1\nNo=0 "));
    if(r==1):
        periodo(lista);
else: 
    mids(n,lista);

        


        
        
        

