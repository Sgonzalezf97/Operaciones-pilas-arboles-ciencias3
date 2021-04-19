'''class Listap:
    def __init__(self, valor, anterior=None):
        self.valor=valor 
        self.anterior=anterior'''

class Nodo:
        def __init__(self,valor,izquierda=None, derecha=None):
            self.valor = valor
            self.izquierda = izquierda
            self.derecha = derecha

def apilar(pila, elemento):
    if pila==None:
       pila= elemento
    else:
        elemento.anterior=pila 
        pila=elemento
    return pila 

def desapilar(pila):
    if pila==None:
       elemento= None
    else:
        elemento=pila.valor
        pila=pila.anterior
    return elemento, pila

def mostrar_pila(pila):
    if pila==None:
        pass
    else: 
        print(pila.valor)
        mostrar_pila(pila.anterior)


def evaluar(arbol):
    if arbol == None:
        pass
    else:
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        if arbol.valor == '-':
            return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
        if arbol.valor == '*':
            return evaluar(arbol.izquierda) * evaluar(arbol.derecha)
        if arbol.valor == '/':
            return evaluar(arbol.izquierda) // evaluar(arbol.derecha)
        return int(arbol.valor)

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+','-','*','/']:
        return "("+ en_orden(arbol.izquierda) + ' ' + str(arbol.valor) + ' ' + en_orden(arbol.derecha) + ")"
    else:
        return str(arbol.valor)

def calcular(Lista):
    contador=0
    while len(val)!= 0:
        if len(val)<3:
            valoropera= val.pop()
            expresion2= Nodo(valoropera,Nodo(resultados[0]),Nodo(resultados[1]))
            print(en_orden(expresion2)+ '=' + str(evaluar(expresion2)))
            resultados.pop(0)
            resultados.pop(0)
            f = open("escritura.txt", "a")
            f.write(str(en_orden(expresion2)+ '=' + str(evaluar(expresion2))))
            f.close
        elif  val[contador] == '-' or val[contador] == '+' or val[contador] == '*' or val[contador] == '/' : 
            valorizquierdo = val[contador-2]
            valorderecho = val[contador-1]
            valoropera = val[contador]
            val.pop(contador)
            val.pop(contador-1)
            val.pop(contador-2)
            contador = 0
            #print(valorizquierdo+" " + valoropera + " "+ valorderecho)
            expresion = Nodo(valoropera,Nodo(valorizquierdo),Nodo(valorderecho))
            print(en_orden(expresion)+ '=' + str(evaluar(expresion)))
            resultados.append(evaluar(expresion))
            f = open("escritura.txt", "a")
            f.write(str(en_orden(expresion)+ '=' + str(evaluar(expresion))))
            f.close
        else:
            contador = contador+1
            #print ("contador:"+ str(contador))

#Variables globales
pila=None
val = []
resultados = []

f = open("lectura.txt", "r")
for linea in f.readlines():
    val= [str(x)for x in linea.split() ]
    print("\n")
    print(val)
    calcular(val)
    resultados=[]
    f = open("escritura.txt", "a")            
    f.write("\n") 
    f.close()
f.close()

#proceso para convertir en pila
'''while len(val) != 0:
    pila=apilar(pila, Nodo(val[-1]))
    val.pop()
print("pila:")
mostrar_pila(pila)'''

#desapilar la pila
#si es un signo guardarlo como valor pasa al siguiente
#desapilar si es un numero guardarlo como izquierda pasa al siguiente
#desapilar si es un numero guardarlo como derecha pasa al siguiente
#crear un nodo con (valor,izquierda,derecha) y lo opera
#si no operar los valores anteriores
#repetir





