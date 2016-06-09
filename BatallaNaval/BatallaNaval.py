#Hacer un programa que permita jugar batalla naval. Con listas
#(lista de listas -> matríz) La computadora vs. humano

import turtle
import random

t=turtle.Turtle()
u=turtle.Turtle()
v=turtle.Turtle()
w=turtle.Turtle()

def BatallaNaval():
    print ("---BATALLA NAVAL---")
    #---CREACION VARIABLES, LISTAS, DICCIONARIOS---
    DerribadosP1=DerribadosCPU=0
    rango=36
    listaP1=[]
    listaCPU=[]
    colorP1={}
    colorCPU={}
    casilleros={"A1":1,"A2":2,"A3":3,"A4":4,"A5":5,"A6":6,"B1":7,"B2":8,"B3":9,"B4":10,
    "B5":11,"B6":12,"C1":13,"C2":14,"C3":15,"C4":16,"C5":17,"C6":18,"D1":19,"D2":20,
    "D3":21,"D4":22,"D5":23,"D6":24,"E1":25,"E2":26,"E3":27,"E4":28,"E5":29,"E6":30,
    "F1":31,"F2":32,"F3":33,"F4":34,"F5":35,"F6":36}
    posiciones=sorted(casilleros.keys())
    listaCPU=posiciones.copy()
    #---CREAR TABLERO---
    CrearTablero()
    #---UBICAR BARCOS---
    colorP1=UbicacionBarcosP1(listaP1,posiciones,colorP1) 
    colorCPU=UbicacionBarcosCPU(listaCPU,posiciones,colorCPU)
    #---MOVIMIENTO Y CHECKEO---
    while (DerribadosP1<2 and DerribadosCPU<2):
        print("---JUGADA---")
        #---MOV P1---
        movP1=str(input("Ingrese movimiento P1: "))
        DerribadosP1=CheckeoBarcosCPU(movP1,colorP1,casilleros,DerribadosP1)
        #---MOV CPU---
        auxCPU=random.randrange(0,rango)
        movCPU=listaCPU[auxCPU]
        listaCPU.pop(auxCPU)
        rango-=1
        DerribadosCPU=CheckeoBarcosP1(movCPU,colorCPU,casilleros,DerribadosCPU)
    #---FIN DEL JUEGO---
    print("---JUEGO TERMINADO---")
    if DerribadosP1==2:
        print("---GANO P1---")
    elif DerribadosCPU==2:
        print("---GANO CPU---")

def UbicacionBarcosP1(lista,posiciones,color):
    print("---UBICACION---")
    listaaux=[]
    print("---Ingreso de barcos separados por espacios!---")
    barco2=str(input("Ingrese barco de 2: "))
    barco3=str(input("Ingrese barco de 3: "))
##    barco4=str(input("Ingrese barco de 4: "))
    listaaux=barco2.split()+barco3.split()
##    aux=barco2.split()+barco3.split()+barco4.split()
    for item in posiciones:
        if item in listaaux:
              color[item]="green"
        else:
            color[item]="red"
    return color

def UbicacionBarcosCPU(lista,posiciones,color):
    print("---UBICACION---")
    ingreso=False
    listaaux=[]
    casillerosb2CPU={1:"A1 A2",2:"A2 A3",3:"A3 A4",4:"A4 A5",5:"A5 A6",7:"B1 B2",
    8:"B2 B3",9:"B3 B4",10:"B4 B5",11:"B5 B6",13:"C1 C2",14:"C2 C3",15:"C3 C4",
    16:"C4 C5",17:"C5 C6",19:"D1 D2",20:"D2 D3",21:"D3 D4",22:"D4 D5",23:"D5 D6",
    25:"E1 E2",26:"E2 E3",27:"E3 E4",28:"E4 E5",29:"E5 E6",31:"F1 F2",32:"F2 F3",
    33:"F3 F4",34:"F4 F5",35:"F5 F6",6:"A1 B1",12:"A2 B2",18:"A3 B3",24:"A4 B4",
    30:"A5 B5",36:"A6 B6",37:"B1 C1",38:"B2 C2",39:"B3 C3",40:"B4 C4",41:"B5 C5",
    42:"B6 C6",43:"D1 C1",44:"D2 C2",45:"D3 C3",46:"D4 C4",47:"D5 C5",48:"D6 C6",
    49:"D1 E1",50:"D2 E2",51:"D3 E3",52:"D4 E4",53:"D5 E5",54:"D6 E6",55:"E1 F1",
    56:"E2 F2",57:"E3 F3",58:"E4 F4",59:"E5 F5",60:"E6 F6"}
    casillerosb3CPU={1:"A1 A2 A3",2:"A2 A3 A4",3:"A3 A4 A5",4:"A4 A5 A6",7:"B1 B2 B3",
    8:"B2 B3 B4",9:"B3 B4 B5",10:"B4 B5 B6",13:"C1 C2 C3",14:"C2 C3 C4",15:"C3 C4 C5",
    16:"C4 C5 C6",19:"D1 D2 D3",20:"D2 D3 D4",21:"D3 D4 D5",22:"D4 D5 D6",
    25:"E1 E2 E3",26:"E2 E3 E4",27:"E3 E4 E5",28:"E4 E5 E6",31:"F1 F2 F3",
    32:"F2 F3 F4",33:"F3 F4 F5",34:"F4 F5 F6",6:"A1 B1 C1",12:"A2 B2 C2",
    18:"A3 B3 C3",24:"A4 B4 C4",30:"A5 B5 C5",36:"A6 B6 C6",37:"B1 C1 D1",
    38:"B2 C2 D2",39:"B3 C3 D3",40:"B4 C4 D4",41:"B5 C5 D5",42:"B6 C6 D6",
    43:"D1 C1 E1",44:"D2 C2 E2",45:"D3 C3 E3",46:"D4 C4 E4",47:"D5 C5 E5",
    48:"D6 C6 E6",35:"D1 E1 F1",29:"D2 E2 F2",23:"D3 E3 F3",17:"D4 E4 F4",
    11:"D5 E5 F5",5:"D6 E6 F6"}
    casillerosb4CPU={1:"A1 A2 A3 A4",2:"A2 A3 A4 A5",3:"A3 A4 A5 A6",4:"B1 B2 B3 B4",
    5:"B2 B3 B4 B5",6:"B3 B4 B5 B6",7:"C1 C2 C3 C4",8:"C2 C3 C4 C5",9:"C3 C4 C5 C6",          
    10:"D1 D2 D3 D4",11:"D2 D3 D4 D5",12:"D3 D4 D5 D6",13:"E1 E2 E3 E4",
    14:"E2 E3 E4 E5",15:"E3 E4 E5 E6",16:"F1 F2 F3 F4",17:"F2 F3 F4 F5",
    18:"F3 F4 F5 F6",19:"A1 B1 C1 D1",20:"B1 C1 D1 E1",21:"C1 D1 E1 F1",
    22:"A2 B2 C2 D2",23:"B2 C2 D2 E2",24:"C2 D2 E2 F2",25:"A3 B3 C3 D3",
    26:"B3 C3 D3 E3",27:"C3 D3 E3 F3",28:"A4 B4 C4 D4",29:"B4 C4 D4 E4",
    30:"C4 D4 E4 F4",31:"A5 B5 C5 D5",32:"B5 C5 D5 E5",33:"C5 D5 E5 F5",
    34:"A6 B6 C6 D6",35:"B6 C6 D6 E6",36:"C6 D6 E6 F6"}
    print("---Ingreso de barcos CPU!---")
    while (ingreso!=True):
##    ---BARCO DE 2---
        aux2=casillerosb2CPU[random.randrange(1,61)]
##    ---BARCO DE 3---
        aux3=casillerosb3CPU[random.randrange(1,49)]
##    ---BARCO DE 4---
##        aux4=casillerosb4CPU[random.randrange(1,37)]
        barco2=aux2.split()
        barco3=aux3.split()
##        barco4=aux4.split()
        ingreso=True
        for item in barco3:
            if item in barco2:
                ingreso=False
    listaaux=barco2+barco3
##    listaaux=barco2+barco3+barco4
    print(listaaux)
    for item in posiciones:
        if item in listaaux:
              color[item]="green"
        else:
            color[item]="red"
    return color

def CheckeoBarcosP1(mov,color,casilleros,Derribados):
    SeteoPos(t,0,0)
    fila=0
    print("---CHECKEO---")
    if color[mov]=="green":
        Derribados+=1
    t.fillcolor(color[mov])
    ubicacion=casilleros[mov]
    if ubicacion >=1 and ubicacion <=6:
        fila=0
    if ubicacion >=7 and ubicacion <=12:
        fila=1
        ubicacion-=6
    if ubicacion >=13 and ubicacion <=18:
        fila=2
        ubicacion-=12
    if ubicacion >=19 and ubicacion <=24:
        fila=3
        ubicacion-=18
    if ubicacion >=25 and ubicacion <=30:
        fila=4
        ubicacion-=24
    if ubicacion >=31 and ubicacion <=36:
        fila=5
        ubicacion-=30
    t.penup()
    t.setposition(ubicacion*20,20*fila)
    t.pendown()
    t.begin_fill()
    t.bk(20)
    t.lt(90)
    t.fd(20)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(20)
    t.lt(90)
    t.end_fill()
    return Derribados

def CheckeoBarcosCPU(mov,color,casilleros,Derribados):
    SeteoPos(v,0,-150)
    fila=0
    print("---CHECKEO---")
    if color[mov]=="green":
        Derribados+=1
    v.fillcolor(color[mov])
    ubicacion=casilleros[mov]
    if ubicacion >=1 and ubicacion <=6:
        fila=0
    elif ubicacion >=7 and ubicacion <=12:
        fila=1
        ubicacion-=6
    elif ubicacion >=13 and ubicacion <=18:
        fila=2
        ubicacion-=12
    elif ubicacion >=19 and ubicacion <=24:
        fila=3
        ubicacion-=18
    elif ubicacion >=25 and ubicacion <=30:
        fila=4
        ubicacion-=24
    elif ubicacion >=31 and ubicacion <=36:
        fila=5
        ubicacion-=30
    v.penup()
    v.setposition(ubicacion*20,20*fila-150)
    v.pendown()
    v.begin_fill()
    v.bk(20)
    v.lt(90)
    v.fd(20)
    v.rt(90)
    v.fd(20)
    v.rt(90)
    v.fd(20)
    v.lt(90)
    v.end_fill()
    return Derribados

def SeteoPos(var,x,y):
    var.penup()
    var.setposition(x,y)
    var.pendown()

def CrearTablero():
    t.speed(9)
    u.speed(9)
    v.speed(9)
    w.speed(9)
    LetrasTab=["A","B","C","D","E","F"]
    NumerosTab=["1","2","3","4","5","6"]
    u.lt(90)
    w.lt(90)
    v.color("blue")
    w.color("blue")
    SeteoPos(v,0,-150)
    SeteoPos(w,0,-150)
    for i in range(7):
        SeteoPos(t,0,i*20)
        t.fd(120)
        SeteoPos(u,i*20,0)
        u.fd(120)
        SeteoPos(v,0,i*20-150)
        v.fd(120)
        SeteoPos(w,i*20,0-150)
        w.fd(120)
    SeteoPos(t,0,0)
    SeteoPos(u,0,0)
    SeteoPos(v,0,-150)
    SeteoPos(w,0,-150)
    for i in range(6):
        SeteoPos(t,i*20+5,-15)
        t.write(NumerosTab[i])
        SeteoPos(u,-15,i*20+5)
        u.write(LetrasTab[i])
        SeteoPos(v,i*20+5,-15-150)
        v.write(NumerosTab[i])
        SeteoPos(w,-15,i*20+5-150)
        w.write(LetrasTab[i])
    t.hideturtle()
    u.hideturtle()
    v.hideturtle()
    w.hideturtle()

BatallaNaval()
