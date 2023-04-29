
class NodoBinario:

    __hijoIzquierdo=None;
    __hijoDerecho = None;
    __dato=0;


    
    def __init__(self,dato):
        self.__dato=dato;
        self.__hijoIzquierdo=None;
        self.__hijoDerecho=None;


    
    def getDato(self):
        return self.__dato;


    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo;

    def getHijoDerecho(self):

        return self.__hijoDerecho


    def setDato(self,dato):
        self.__dato=dato;

    def setHijoDerecho(self,nodo):
        self.__hijoDerecho=nodo;


    def setHijoIzquierdo(self,nodo):
        self.__hijoIzquierdo=nodo;


    def esHoja(self):
        return self.__hijoDerecho==None and self.__hijoIzquierdo == None;   




    def prueba():
        return 0;