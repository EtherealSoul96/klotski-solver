

from copy import deepcopy


piece_width    = 8
piece_height   = 4
horizontal_gap = 2
vertical_gap   = 1
symbol = "█"

tablero_vacio = (
    [
        [symbol for j in range(6 * piece_width - horizontal_gap)]
        for i in range(piece_height - vertical_gap)
    ] +
    [
        [symbol for j in range(    piece_width - horizontal_gap)] +
        [" "    for j in range(4 * piece_width + horizontal_gap)] +
        [symbol for j in range(    piece_width - horizontal_gap)]
        for i in range(5 * piece_height + vertical_gap)
    ] +
    [
        [symbol for j in range(2 * piece_width - horizontal_gap)] +
        [" "    for j in range(2 * piece_width + horizontal_gap)] +
        [symbol for j in range(2 * piece_width - horizontal_gap)]
        for i in range(piece_height - vertical_gap)
    ]
)

tamaños = [
    (2, 2),
    (1, 2),
    (1, 2),
    (1, 2),
    (1, 2),
    (2, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
]

def print_tablero(tablero):

    texto = deepcopy(tablero_vacio)

    for i, (x, y) in enumerate(tablero[:-2]):
        x = x * piece_width
        y = y * piece_height

        dx, dy = tamaños[i]
        dx = dx * piece_width  - horizontal_gap
        dy = dy * piece_height - vertical_gap

        for x2 in range(x, x + dx):
            for y2 in range(y, y + dy):
                texto[y2][x2] = symbol

    print("\n".join(
        ["".join(row) for row in texto]
    ))
    print("\n" * piece_height)

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
    if xs==x0i and ys==y0i-1 and not u in lista_movimientos:
            ys=ys+1
            y0i=y0i-1
            lista_movimientos.append(u)
            mov2=d
    elif xs == x0i and ys==y0i+1 and not d in lista_movimientos:
            ys=ys-1
            y0i=y0i+1
            lista_movimientos.append(d)
            mov2 = u
    elif ys==y0i and xs==x0i-1and not r in lista_movimientos:
            xs = xs + 1
            x0i = x0i - 1
            lista_movimientos.append(r)
            mov2 = l
    elif ys == y0i and xs==x0i+1 and not l in lista_movimientos:
            xs=xs-1
            x0i=x0i+1
            lista_movimientos.append(l)
            mov2 = r
    return xs,ys,x0i,y0i,mov2

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


tablero=((xl,yl),(xv1,yv1),(xv2,yv2),(xv3,yv3),(xv4,yv4),(xh,yh),(xs1,ys1),(xs2,ys2),(xs3,ys3),(xs4,ys4),(x01,y01),(x02,y02))
espacios_vacios=((x01,y01),(x02,y02))

dic_tableros={}
lista_movimientos=[]
map=[]

print("moves:", 0, 0)
print_tablero(tablero)

#----------------------------------------------------------------------------
for i in range(10000):

    v0=h0=0
        #Orientacion espacios vacios
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
    elif yh == y01 and xh == x01 - 2 and not "hr" in lista_movimientos:
        xh = xh + 1
        x01 = x01 - 2
        lista_movimientos.append("hr")
        mov2 = "hl"
    elif yh == y02 and xh == x02 - 2 and not "hr" in lista_movimientos:
        xh = xh + 1
        x02 = x02 - 2
        lista_movimientos.append("hr")
        mov2 = "hl"
    elif yh == y01 and xh == x01 + 1 and not "hl" in lista_movimientos:
        xh = xh - 1
        x01 = x01 + 2
        lista_movimientos.append("hl")
        mov2 = "hr"
    elif yh == y02 and xh == x02 + 1 and not "hl" in lista_movimientos:
        xh = xh - 1
        x02 = x02 + 2
        lista_movimientos.append("hl")
        mov2 = "hr"
    #doble-----------------------------------------------
    elif yv1==v0 and (xv1==x01-1 and not "v1r" in lista_movimientos or xv1==x01+1 and not "v1l" in lista_movimientos):
        xv1,x01,x02,mov2=verticales_doble(xv1,x01,x02,"v1r","v1l")
    elif yv2==v0 and (xv2==x01-1 and not "v2r" in lista_movimientos or xv2==x01+1 and not "v2l" in lista_movimientos):
        xv2,x01,x02,mov2=verticales_doble(xv2,x01,x02,"v2r","v2l")
    elif yv3==v0 and (xv3==x01-1 and not "v3r" in lista_movimientos or xv3==x01+1 and not "v3l" in lista_movimientos):
        xv3,x01,x02,mov2=verticales_doble(xv3,x01,x02,"v3r","v3l")
    elif yv4==v0 and (xv4==x01-1 and not "v4r" in lista_movimientos or xv4==x01+1 and not "v4l" in lista_movimientos):
        xv4,x01,x02,mov2=verticales_doble(xv4,x01,x02,"v4r","v4l")
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
        xs1,ys1,x01,y01,mov2=cuadrados(xs1,ys1,x01,y01,"s1u","s1d","s1r","s1l")
    elif xs2==x01 and (ys2==y01-1 and not "s2u" in lista_movimientos or ys2==y01+1 and not "s2d" in lista_movimientos) or ys2==y01 and (xs2==x01-1 and not "s2r" in lista_movimientos or xs2==x01+1 and not "s2l" in lista_movimientos):
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
        dic_tableros[tablero]=lista_movimientos
        map.pop()
        tablero=map[len(map)-1]
        ((xl, yl), (xv1, yv1), (xv2, yv2), (xv3, yv3), (xv4, yv4), (xh, yh), (xs1, ys1), (xs2, ys2), (xs3, ys3),
        (xs4, ys4),(x01,y01),(x02,y02)) = tablero
        lista_movimientos=dic_tableros[tablero]
        no_jugada = True

    if not no_jugada:
        tablero = ((xl, yl), (xv1, yv1), (xv2, yv2), (xv3, yv3), (xv4, yv4), (xh, yh), (xs1, ys1), (xs2, ys2), (xs3, ys3), (xs4, ys4),(x01,y01),(x02,y02))
        map.append(tablero)
        if tablero in dic_tableros:
            lista_movimientos = dic_tableros[tablero]
        else:
            lista_movimientos = []
        lista_movimientos.append(mov2)
        dic_tableros[tablero] = lista_movimientos

    no_jugada = False

    print(f"moves: {i + 1}, {len(map)}")
    print_tablero(tablero)


    if xl == 2 and yl==4:
        print("won!!!")
        break
