from stringprep import c22_specials

# La clase es solo una etiqueta.

def Clasificador(x1, x2): 
    h = -8*x1 - 5*x2 + 4
    if h >= 0:
        clase="c1"
    else:
        clase="c2"
    return print("Pertenece a: " + clase)

x1 = 0
x2 = 0

Clasificador(x1,x2)