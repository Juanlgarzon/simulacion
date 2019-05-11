#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Metodos de Montecarlo y del Trapecio
import random
import math

def mtc(n):
    suma=0;
    i=0;
    while i < n:
    
        x=2*random.random();
        y=2*math.exp(-x*x);
        suma+=y;
        i += 1;
     
    return(suma/n);   


def trap(paso):
    x1=0;
    x2=paso;
    suma=0;
    
    while x2 <= 2:
        fx2=math.exp(-x2*x2);
        tria=((math.exp(-x1*x1)) - fx2)*(paso/2);
        suma=suma+tria+(fx2*paso);
        x1=x2;
        x2=x2+paso;
     
    return(suma);

print("metodos de Montecarlo y del trapecio:\n ");
n=float(input("Introduce el valor de n para el metodo de Montecarlo: "));
pas=float(input("Introduce el valor del paso para el metodo del trapecio: "));
r1=round(mtc(n),6);
r2=round(trap(pas),6);
r=0.882081;
print("El resultado previamente desarrollado es = ",r);
print("El resultado mediante el metodo de Montecarlo= ",r1);
print("El resultado mediante el metodo del trapecio= ",r2);
s1=abs(r-r1);
s2=abs(r-r2);

if(s1<s2):
    
    print("\nEl metodo de Montecarlo es el mas aproximado");
else:
    print("\nEl metodo del trapecio resulta ser mas aproximado");

