class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def IntersectionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """
    # sem doplnte kod funkce, dalsi casti zdrojoveho kodu NEMENTE

    result = Prvek(0, None)
    tail = result

    while a != None and b != None:
        if a.x == b.x:
            tail.dalsi = a
            tail = tail.dalsi
            a = a.dalsi
            b = b.dalsi
        elif a.x < b.x:
            a = a.dalsi
        else:
            b = b.dalsi

    tail.dalsi = None
    return result.dalsi


#################################################

VytiskniLSS( IntersectionDestruct( NactiLSS(), NactiLSS() ) )
