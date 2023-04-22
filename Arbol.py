from collections import deque
from inspect import stack
from Nodo import NodoBinario;

class Arbol:

    __raiz=None;

    def __init__(self):
        self.__raiz=None;

    

    def esVacio(self):
        return self.__raiz==None;

    def insertar(self,datoInsertar):
        if(self.esVacio()):
            nuevo = NodoBinario(datoInsertar);
            self.__raiz=nuevo
            return
        else:
            actual = self.__raiz
            anterior = None
            while(actual is not None):
                anterior=actual
                if datoInsertar < actual.getDato():
                    actual=actual.getHijoIzquierdo()
                elif datoInsertar > actual.getDato():
                   
                    actual=actual.getHijoDerecho()
                else:
                    print("El dato el se encuentra en el arbol")
                    return;                                                                                           
            nuevo = NodoBinario(datoInsertar)
            if datoInsertar < anterior.getDato():
               
                anterior.setHijoIzquierdo(nuevo)
                
            else:
                anterior.setHijoDerecho(nuevo)




    def recorridoNiveles(self):
        cola =deque()
        
        if self.esVacio() == False:
            cola.append(self.__raiz)
            while(cola.__len__()>0):
                nodo = cola.popleft()
             
                print(nodo.getDato())
                # print(cola.__len__())
              
                if(nodo.getHijoIzquierdo() is not None):
                    cola.append(nodo.getHijoIzquierdo())
                if (nodo.getHijoDerecho() is not None):
                    cola.append(nodo.getHijoDerecho())
     
    

    # def recorridoInOrden(self):
    #     pila = stack();
    #     self.meterPila(stack,self.__raiz)
    #     while(pila.__len__()>0):
    #         nodo = pila.pop();
    #         if(nodo.getHijoIzquierdo() is not None):

            