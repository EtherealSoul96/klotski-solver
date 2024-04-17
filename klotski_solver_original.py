#def verticales_doble(xv,yv,y01,y02):
    #if yv==v0:

def verticales_doble(xv,x01,x02,r,l):
    if xv==x01-1 and not r in lista_movimientos:
        xv=xv+1
        x01=x01-1
        x02=x02-1
        lista_movimientos.append(r)
        mov2=l
    elif xv==x01+1 and not l in lista_movimientos:
        xv=xv-1
        x01=x01+1
        x02=x02+1
        lista_movimientos.append(l)
        mov2=r
    return xv,x01,x02,mov2

"""
def verticales_simple(xv,yv,y01,y02):
    for [x0i,y0i] in ([x01,y01],[x02,y02]):
        if xv==x0i:
            if yv==y0i-2:
                yv=yv+1
                y0i=y0i-2
                ban = 1
            if yv==y0i+2:
                yvi=yv-1
                y0i=y0i+2
                ban = 1

    return yv,y01,y02
"""

def verticales_simple(yv,y0i,u,d):
    if yv==y0i-2 and not u in lista_movimientos:
        yv=yv+1
        y0i=y0i-2
        lista_movimientos.append(u)
        mov2=d
    elif yv==y0i+1 and not d in lista_movimientos:
        yv=yv-1
        y0i=y0i+2
        lista_movimientos.append(d)
        mov2=u
    return yv,y0i,mov2

def cuadrados(xs,ys,x0i,y0i,u,d,r,l):
#    if ban==0:
    if xs==x0i and ys==y0i-1 and not u in lista_movimientos:
            ys=ys+1
            y0i=y0i-1
            lista_movimientos.append(u)
            mov2=d
            #print("es falso1")
            #ban=1
            #return(x0i,y0i,xs,ys)
    elif xs == x0i and ys==y0i+1 and not d in lista_movimientos:
            ys=ys-1
            y0i=y0i+1
            lista_movimientos.append(d)
            mov2 = u
            #print("es falso2")
            #ban=1
            #return(x0i,y0i,xs,ys)
    elif ys==y0i and xs==x0i-1and not r in lista_movimientos:
            xs = xs + 1
            x0i = x0i - 1
            lista_movimientos.append(r)
            mov2 = l
            #print(xs, ys, x0i, y0i)
            #print(xs1, ys1, x01, x02)
            #print("es verdad")
            #ban = 1
            #return(x0i,y0i,xs,ys)
    elif ys == y0i and xs==x0i+1 and not l in lista_movimientos:
            xs=xs-1
            x0i=x0i+1
            lista_movimientos.append(l)
            mov2 = r
    return xs,ys,x0i,y0i,mov2

#            print("es falso3")
#            ban=1
#            return(x0i,y0i,xs,ys)
#        else:
#            print("why?")

"""               
def cuadrados(x0i,y0i,xs,ys,ban):
    if ban==0:
        if xs==x0i:
            if ys==y0i-1:
                ys=ys+1
                y0i=y0i-1
                print("es falso1")
                ban=1
                return(x0i,y0i,xs,ys)
            elif ys==y0i+1:
                ys=ys-1
                y0i=y0i+1
                print("es falso2")
                ban=1
                return(x0i,y0i,xs,ys)
        elif ys==y0i:
            if xs==x0i-1:
                print(xs, ys, x0i, y0i)
                xs = xs + 1
                x0i = x0i - 1
                print(xs, ys, x0i, y0i)
                print(xs1, ys1, x01, x02)
                print("es verdad")
                ban = 1
                return(x0i,y0i,xs,ys)
            elif xs==x0i+1:
                xs=xs-1
                x0i=x0i+1
                print("es falso3")
                ban=1
                return(x0i,y0i,xs,ys)
        else:
            print("why?")

    return x0i,y0i,xs,ys
"""


xl=2
yl=1

xv1=1
yv1=1

xv2=4
yv2=1

xv3=1
yv3=3

xv4=4
yv4=3

xh=2
yh=3

xs1=1
ys1=5

xs2=2
ys2=4

xs3=3
ys3=4

xs4=4
ys4=5

x01=2
y01=5

x02=3
y02=5

mov2=0
no_jugada=False
x=0

#g=0 v=1:4 h=5 s=6:9
#tablero_original=[([xl,yl],[xl,yl+1],[xl+1,yl],[xl+1,yl+1]),([xv1,yv1],[xv1,yv1+1]),([xv2,yv2],[xv2,yv2+1]),([xv3,yv3],[xv3,yv3+1]),([xv4,yv4],[xv4,yv4+1]),([xh,yh],[xh+1,yh]),([xs1,ys1]),([xs2,ys2]),([xs3,ys3]),([xs4,ys4])]
#tablero2=[(["xl","yl"],[xl,yl+1],[xl+1,yl],[xl+1,yl+1]),(["xv1","yv1"],[xv1,yv1+1]),(["xv2","yv2"],[xv2,yv2+1]),(["xv3","yv3"],[xv3,yv3+1]),(["xv4","yv4"],[xv4,yv4+1]),(["xh","yh"],[xh+1,yh]),(["xs1","ys1"]),(["xs2","ys2"]),(["xs3","ys3"]),(["xs4","ys4"])]


tablero=((xl,yl),(xv1,yv1),(xv2,yv2),(xv3,yv3),(xv4,yv4),(xh,yh),(xs1,ys1),(xs2,ys2),(xs3,ys3),(xs4,ys4),(x01,y01),(x02,y02))
espacios_vacios=((x01,y01),(x02,y02))

dic_tableros={}
lista_movimientos=[]
anulados=[]
map=[]
print(tablero)
print(espacios_vacios)


#lista_movimientos=[12,16,36]


#lu,ld,lr,ll,v1u,v1d,v1r,v1l,v2u,v2d,v2r,v2l,v3u,v3d,v3r,v3l,v4u,v4d,v4r,v4l,hu,hd,hr,hl,s1u,s1d,s1r,s1l,s2u,s2d,s2r,s2l,s3u,s3d,s3r,s3l,s4u,s4d,s4r,s4l,
#for [coordenada_name,coordenada_valor], in []
#    if coordenada_name in lista_movimientos:
#        coordenada_valor = 1

#----------------------------------------------------------------------------
for i in range (50):
    if i==9999:
        print(tablero,lista_movimientos)
    v0=h0=0
        #Orintacon espacios vacios
    if y01==y02 and x01==x02-1:
        orientacion_espacios_vacios=1 #horizontal
        h0=x01
    elif y01==y02 and x01==x02+1:
        orientacion_espacios_vacios=1 #horizontal
        h0=x02
    elif x01==x02 and (y01==y02-1):
        orientacion_espacios_vacios=2 #vertical
        v0=y01
    elif x01==x02 and (y01==y02+1):
        orientacion_espacios_vacios=2 #vertical
        v0=y02
    else:
        orientacion_espacios_vacios=3
        h0=0
        v0=0
    #-------------------------------------------------------------------------------
    #ban=0
    #if orientacion_espacios_vacios==1:------------------------

    if xl==h0 and yl==y01-2 and not "lu" in lista_movimientos: #grande abajo
        #ficha0abajo(tablero[0],espacios_vacios)    "bajar fiha grande"
        yl=yl+1
        y01=y01-2
        y02=y02-2
        lista_movimientos.append("lu")
        mov2 = "ld"
    elif xh==h0 and yh==y01-1 and not "hu" in lista_movimientos:
            yh=yh+1
            y01=y01-1
            y02=y02-1
            lista_movimientos.append("hu")
            mov2="hd"
    elif xh==h0 and yh==y01+1 and not "hd" in lista_movimientos:
            yh=yh-1
            y01=y01+1
            y02=y02+1
            lista_movimientos.append("hd")
            mov2 = "hu"
    #if orientacion_espacios_vacios==2:------------------------
    elif yl==v0 and xl==x01-2 and not "lr" in lista_movimientos: #grande <-- -->
                xl=xl+1
                x01=x01-2
                x02=x02-2
                lista_movimientos.append("lr")
                mov2 = "ll"
    elif yl==v0 and xl==x01+1 and not "ll" in lista_movimientos:
                xl=xl-1
                x01=x01+2
                x02=x02+2
                lista_movimientos.append("ll")
                mov2 = "lr"
    # horizontal <--- --->
    elif yh==y01 and (((xh==x01-2 or xh==x02-2) and not "hr" in lista_movimientos) or (xh==x01+1 or xh==x02+1) and not "hl" in lista_movimientos):
            if xh==x01-2:
                xh=xh+1
                x01=x01-2
                lista_movimientos.append("hr")
                mov2 = "hl"
            elif xh==x02-2:
                xh=xh+1
                x02=x02-2
                lista_movimientos.append("hr")
                mov2 = "hl"
            elif xh==x01+1:
                xh=xh-1
                x01=x01+2
                lista_movimientos.append("hl")
                mov2 = "hr"
            elif xh==x02+1:
                xh=xh-1
                x02=x02+2
                lista_movimientos.append("hl")
                mov2 = "hr"
            print(lista_movimientos,'  ',tablero,"fsldjfsgasaogaosdg")
    #doble-----------------------------------------------
    elif yv1==v0 and (xv1==x01-1 and not "v1r" in lista_movimientos or xv1==x01+1 and not "v1l" in lista_movimientos):
        xv1,y01,y02,mov2=verticales_doble(xv1,x01,x02,"v1r","v1l")
    elif yv2==v0 and (xv2==x01-1 and not "v2r" in lista_movimientos or xv2==x01+1 and not "v2l" in lista_movimientos):
        xv2,y01,y02,mov2=verticales_doble(xv2,x01,x02,"v2r","v2l")
    elif yv3==v0 and (xv3==x01-1 and not "v3r" in lista_movimientos or xv3==x01+1 and not "v3l" in lista_movimientos):
        print(yv3,v0,tablero)
        xv3,y01,y02,mov2=verticales_doble(xv3,x01,x02,"v3r","v3l")
    elif yv4==v0 and (xv4==x01-1 and not "v4r" in lista_movimientos or xv4==x01+1 and not "v4l" in lista_movimientos):
        xv4,y01,y02,mov2=verticales_doble(xv4,x01,x02,"v4r","v4l")
    #simples-------------------------------------------
    elif xv1==x01 and (yv1==y01-2 and not "v1u" in lista_movimientos or yv1==y01+1 and not "v1d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv1,y01,mov2=verticales_simple(yv1,y01,"v1u","v1d")
    elif xv2==x01 and (yv2==y01-2 and not "v2u" in lista_movimientos or yv2==y01+1 and not "v2d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv2,y01,mov2=verticales_simple(yv2,y01,"v2u","v2d")
    elif xv3==x01 and (yv3==y01-2 and not "v3u" in lista_movimientos or yv3==y01+1 and not "v3d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv3,y01,mov2=verticales_simple(yv3,y01,"v3u","v3d")
    elif xv4==x01 and (yv4==y01-2 and not "v4u" in lista_movimientos or yv4==y01+1 and not "v4d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv4,y01,mov2=verticales_simple(yv4,y01,"v4u","v4d")
    elif xv1==x02 and (yv1==y02-2 and not "v1u" in lista_movimientos or yv1==y02+1 and not "v1d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv1,y02,mov2=verticales_simple(yv1,y02,"v1u","v1d")
    elif xv2==x02 and (yv2==y02-2 and not "v2u" in lista_movimientos or yv2==y02+1 and not "v2d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv2,y02,mov2=verticales_simple(yv2,y02,"v2u","v2d")
    elif xv3==x02 and (yv3==y02-2 and not "v3u" in lista_movimientos or yv3==y02+1 and not "v3d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv3,y02,mov2=verticales_simple(yv3,y02,"v3u","v3d")
    elif xv4==x02 and (yv4==y02-2 and not "v4u" in lista_movimientos or yv4==y02+1 and not "v4d" in lista_movimientos):#----------------------------------------------------   -1 o -2?????
        yv4,y02,mov2=verticales_simple(yv4,y02,"v4u","v4d")
    #cuadrados------------------------------------------------------
    elif xs1==x01 and (ys1==y01-1 and not "s1u" in lista_movimientos or ys1==y01+1 and not "s1d" in lista_movimientos) or ys1==y01 and (xs1==x01-1 and not "s1r" in lista_movimientos or xs1==x01+1 and not "s1l" in lista_movimientos):
        print("problemas",tablero)
        xs1,ys1,x01,y01,mov2=cuadrados(xs1,ys1,x01,y01,"s1u","s1d","s1r","s1l")
    elif xs2==x01 and (ys2==y01-1 and not "s2u" in lista_movimientos or ys2==y01+1 and not "s2d" in lista_movimientos) or ys2==y01 and (xs2==x01-1 and not "s2r" in lista_movimientos or xs2==x01+1 and not "s2l" in lista_movimientos):
        print("problemas2", tablero)
        xs2,ys2,x01,y01,mov2=cuadrados(xs2,ys2,x01,y01,"s2u","s2d","s2r","s2l")
    elif xs3==x01 and (ys3==y01-1 and not "s3u" in lista_movimientos or ys3==y01+1 and not "s3d" in lista_movimientos) or ys3==y01 and (xs3==x01-1 and not "s3r" in lista_movimientos or xs3==x01+1 and not "s3l" in lista_movimientos):
        xs3,ys3,x01,y01,mov2=cuadrados(xs3,ys3,x01,y01,"s3u","s3d","s3r","s3l")
    elif xs4==x01 and (ys4==y01-1 and not "s4u" in lista_movimientos or ys4==y01+1 and not "s4d" in lista_movimientos) or ys4==y01 and (xs4==x01-1 and not "s4r" in lista_movimientos or xs4==x01+1 and not "s4l" in lista_movimientos):
        xs4,ys4,x01,y01,mov2=cuadrados(xs4,ys4,x01,y01,"s4u","s4d","s4r","s4l")
    elif xs1==x02 and (ys1==y02-1 and not "s1u" in lista_movimientos or ys1==y02+1 and not "s1d" in lista_movimientos) or ys1==y02 and (xs1==x02-1 and not "s1r" in lista_movimientos or xs1==x02+1 and not "s1l" in lista_movimientos):
        xs1,ys1,x02,y02,mov2=cuadrados(xs1,ys1,x02,y02,"s1u","s1d","s1r","s1l")
    elif xs2==x02 and (ys2==y02-1 and not "s2u" in lista_movimientos or ys2==y02+1 and not "s2d" in lista_movimientos) or ys2==y02 and (xs2==x02-1 and not "s2r" in lista_movimientos or xs2==x02+1 and not "s2l" in lista_movimientos):
        xs2,ys2,x02,y02,mov2=cuadrados(xs2,ys2,x02,y02,"s2u","s2d","s2r","s2l")
    elif xs3==x02 and (ys3==y02-1 and not "s3u" in lista_movimientos or ys3==y02+1 and not "s3d" in lista_movimientos) or ys3==y02 and (xs3==x02-1 and not "s3r" in lista_movimientos or xs3==x02+1 and not "s3l" in lista_movimientos):
        xs3,ys3,x02,y02,mov2=cuadrados(xs3,ys3,x02,y02,"s3u","s3d","s3r","s3l")
    elif xs4==x02 and (ys4==y02-1 and not "s4u" in lista_movimientos or ys4==y02+1 and not "s4d" in lista_movimientos) or ys4==y02 and (xs4==x02-1 and not "s4r" in lista_movimientos or xs4==x02+1 and not "s4l" in lista_movimientos):
        xs4,ys4,x02,y02,mov2=cuadrados(xs4,ys4,x02,y02,"s4u","s4d","s4r","s4l")
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!!!

    elif orientacion_espacios_vacios==1 and xl==h0 and yl==y01+1 and not "ld" in lista_movimientos: #grande arriba
            yl=yl-1
            y01=y01+2
            y02=y02+2
            lista_movimientos.append("ld")
            mov2="lu"
    else:
        print("no hay movimientos posibles")
        #mov2=0
        #dic_tableros.remove(tablero)
        #anulados.append[tablero]
        dic_tableros[tablero]=lista_movimientos
        #print(lista_movimientos,"algo?")
        map.remove(tablero)
        tablero=map[len(map)-1]
        ((xl, yl), (xv1, yv1), (xv2, yv2), (xv3, yv3), (xv4, yv4), (xh, yh), (xs1, ys1), (xs2, ys2), (xs3, ys3),
        (xs4, ys4),(x01,y01),(x02,y02)) = tablero
        lista_movimientos=dic_tableros[tablero]
        no_jugada=True
        #print(lista_movimientos,"aca")

        # tablero=index dic_tableros[tablero]-1
    x = x + 1
    print(lista_movimientos,'   ',tablero,x,'  ',i)


    #dic_tableros[tablero]=lista_movimientos
    if not no_jugada:
        tablero = ((xl, yl), (xv1, yv1), (xv2, yv2), (xv3, yv3), (xv4, yv4), (xh, yh), (xs1, ys1), (xs2, ys2), (xs3, ys3), (xs4, ys4),(x01,y01),(x02,y02))
        map.append(tablero)
        if tablero in dic_tableros:
            lista_movimientos = dic_tableros[tablero]
        else:
            lista_movimientos = []
        lista_movimientos.append(mov2)
        dic_tableros[tablero] = lista_movimientos
    no_jugada=False
    #espacios_vacios = [([x01], [y01]), ([x02], [y02])]
#        dic_tableros.append(*movimiento*) s1u
    #print(tablero,espacios_vacios)
    #print(mov2,"holaaa")
    #FIJARSE Q VARIABLES NESESITAN REFRESCAR SU VALOR ANTES DEL FOR
    """        if ban == 0:
                xv1,y01,y02=verticales_doble(xv1,yv1,y01,y02)
            if ban == 0:
                xv2,y01,y02=verticales_doble(xv2,yv2,y01,y02)
            if ban == 0:
                xv3,y01,y02=verticales_doble(xv3,yv3,y01,y02)
            if ban == 0:
                xv4,y01,y02=verticales_doble(xv4,yv4,y01,y02)"""


    """    
        if ban==0:
            yv1,y01,y02=verticales_simple(xv1,yv1,y01,y02)
        if ban==0:
            yv2,y01,y02=verticales_simple(xv2,yv2,y01,y02)
        if ban==0:
            yv3,y01,y02=verticales_simple(xv3,yv3,y01,y02)
        if ban==0:
            yv4,y01,y02=verticales_simple(xv4,yv4,y01,y02)
        """

"""
for [x0i,y0i] in ([x01,y01],[x02,y02]):
    if yh==y0i:
        if xh==x0i-2:
            xh=xh+1
            x0i=x0i-2
        if xh==x0i+1:
            xh=xh-1
            x0i=x0i+2
"""

#for [xs,ys] in ([xs1,ys1],[xs2,ys2],[xs3,ys3],[xs4,ys4]):
#    for [x0i, y0i] in ([x01, y01], [x02, y02]):
#        if ban==0:
#            x0i,y0i,xs,ys,ban=cuadrados(x0i,y0i,xs,ys,0)
"""
if ban==0:
    x01,y01,xs1,ys1,ban=cuadrados(x01,y01,xs1,ys1,0)
    



if ban==0:
    x01,y01,xs2,ys2,ban=cuadrados(x01,y01,xs2,ys2,0)
if ban == 0:
    x01,y01,xs3,ys3,ban=cuadrados(x01,y01,xs3,ys3,0)
if ban == 0:
    x01,y01,xs4,ys4,ban=cuadrados(x01,y01,xs4,ys4,0)
if ban == 0:
    x02,y02,xs1,ys1,ban=cuadrados(x02,y02,xs1,ys1,0)
if ban == 0:
    x02,y02,xs2,ys2,ban=cuadrados(x02,y02,xs2,ys2,0)
if ban == 0:
    x02,y02,xs3,ys3,ban=cuadrados(x02,y02,xs3,ys3,0)
if ban == 0:
    x02,y02,xs4,ys4,ban=cuadrados(x02,y02,xs4,ys4,0)
"""
"""
        if bandera==0:
            if xs==x0i:
                if ys==y0i-1:
                    ys=ys+1
                    y0i=y0i-1
                    print("es falso1")
                    bandera=1
                elif ys==y0i+1:
                    ys=ys-1
                    y0i=y0i+1
                    print("es falso2")
                    bandera=1
            elif ys==y0i:
                if xs==x0i-1:
                    print(xs,ys,x0i,y0i)
                    xs=xs+1
                    x0i=x0i-1
                    print(xs,ys,x0i,y0i)
                    print(xs1,ys1,x01,x02)
                    print("es verdad")
                    bandera=1
                elif xs==x0i+1:
                    xs=xs-1
                    x0i=x0i+1
                    print("es falso3")
                    bandera=1
"""




#print (orientacion_espacios_vacios)
#print(tablero2)

#x01,y01,xs1,ys1=cuadrados(x0i,y0i,xs,ys)

#print((xs1,ys1,x01,y01))