protagonista={"salud":100, "tipo":"protagonista"}
monstruo={"salud":3, "tipo" :"monstruo"}
mundo=[None]*30
mundo[9]=monstruo
mundo[10]=protagonista
ubicaciones={}
ubicaciones["protagonista"]=10
ubicaciones["monstruo"]=9

def print_ (p):
    print (p, end ="")


def imprimir (mundo, posicion):
    if posicion<0:
        print_ ("[")
        return 
    elif (posicion>=len(mundo)):
        print_ ("]")
        return
    p= mundo [posicion]
    if p is None:
        print_("[]")
    elif "tipo" in p:
        if p ["tipo"]=="protagonista":
            print_ ("[P]")
        elif p["tipo"]=="monstruo":
            print_ ("[M]")
            

def ver (mundo, ubicaciones):
    """imprime por medio del metodo imprimir dos casillas al rededor del
protagonista el cual es una entrada en el diccionario ubicaciones"""
    p=ubicaciones["protagonista"]
    l=[p-2, p-1, p, p+1, p+2]
    imprimir (mundo, l[0])
    imprimir (mundo, l[1])
    imprimir (mundo, l[2])
    imprimir (mundo, l[3])
    imprimir (mundo, l[4])
    print ()
    
ver (mundo, ubicaciones)

def es_monstruo (casilla):
    if casilla is None :
        return False
    if ("tipo" in casilla):
        return "monstruo" == casilla ["tipo"]
    return False 

def alrededor (p, mundo):
    l= None
    if p==0:
        l=mundo[p+1]
    elif p==len (mundo)-1:
        l=mundo [p-1]
    else: 
        l=[mundo[p-1], mundo[p+1]]
    return l

def bajar_salud(casilla,cuanto):
    casilla["salud"]=casilla["salud"] - cuanto

def atacar (mundo, ubicaciones):
    """este metodo checa primero si hay un monstruo al rededor del protagonista.
si no hay ninguno, no pasa nada.
si hay uno o mas monstruos a su alrrededor decrementa su salud por un punto
a cada
uno."""
    p=ubicaciones["protagonista"]
    lugares=alrededor(p,mundo)
    if es_monstruo(lugares[0]):
        bajar_salud (lugares[0], 1)    
    if len (lugares)==2:
        if es_monstruo(lugares[1]):
            bajar_salud (lugares[1], 1)
    
print (monstruo)
atacar (mundo, ubicaciones)
atacar (mundo, ubicaciones)
atacar (mundo, ubicaciones)
print (monstruo)
print (mundo)
