from stringprep import c22_specials

# La clase es solo una etiqueta.
# si x>=0 entonces c1 && si x<0 entonces c2

def Clasificador(x1, x2): 
    h = -8*x1 -5*x2 + 4 # 1 = -6
    h2 = -4*x1 -5*x2 + 6 # 1 = -3
    if h2 * h >= 0:
        clase="c1"
    else:
        clase="c2"
    return print("Pertenece a: " + clase)

x1 = 1
x2 = 1

Clasificador(x1,x2)