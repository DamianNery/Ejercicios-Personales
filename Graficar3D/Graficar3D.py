#!/usr/bin/env python3
#Graficar en 3D figuras geometricas

import turtle

t=turtle.Turtle()
u=turtle.Turtle()
r=turtle.Turtle()

def DibujarEje():
    t.fd(150)
    DibujarFlecha()
    t.penup()
    t.setposition(0,0)
    t.pendown()

def DibujarFlecha():
    t.begin_fill()
    t.lt(90)
    t.fd(3)
    t.rt(120)
    t.fd(5)
    t.rt(120)
    t.fd(5)
    t.rt(120)
    t.fd(3)
    t.end_fill()

def SeteoPos(var,x,y):
    var.penup()
    var.setposition(x,y)
    var.pendown()    

def CrearCubo(base,altura,profundidad,ancho):
##    t.speed(1)
##    u.speed(1)
##    r.speed(1)    
    t.width(3)
    u.width(3)
    r.width(3)
    t.fd(base)
    SeteoPos(t,0,altura)
    t.fd(base)
    u.fd(altura)
    SeteoPos(u,base,0)
    u.fd(altura)
    r.fd(profundidad)
    txref=uxref=r.xcor()
    tyref=uyref=r.ycor()
    SeteoPos(r,0,altura)
    r.fd(profundidad)
    SeteoPos(r,base,0)
    r.fd(profundidad)
    SeteoPos(r,base,altura)
    r.fd(profundidad)
    SeteoPos(t,txref,tyref)
    t.fd(base)
    SeteoPos(t,txref,tyref+altura)
    t.fd(base)
    SeteoPos(u,txref,tyref)
    u.fd(altura)
    SeteoPos(u,txref+base,tyref)
    u.fd(altura)
    t.hideturtle()
    u.hideturtle()
    r.hideturtle()

def CrearCilindro(radio,profundidad,ancho):
##    t.speed(1)
##    u.speed(1)
##    r.speed(1)
    t.width(3)
    u.width(3)
    r.width(3)
    t.circle(radio)
    u.circle(radio)
    r.circle(radio)
    SeteoPos(r,20,5)
    r.fd(profundidad)
    txref=r.xcor()
    tyref=r.ycor()
    SeteoPos(t,txref,tyref)
    t.circle(radio)
    SeteoPos(r,-20,(radio*2)-5)
    r.fd(profundidad)
    
def CrearPiramide(base,altura,profundidad,ancho):
##    t.speed(1)
##    u.speed(1)
##    r.speed(1)
    t.width(3)
    u.width(3)
    r.width(3)
    t.fd(base)
    r.fd(profundidad)
    txref=r.xcor()
    tyref=r.ycor()
    SeteoPos(t,txref,tyref)
    t.fd(base)
    SeteoPos(r,base,0)
    r.fd(profundidad)
    u.penup()
    u.setposition(0,altura)
    u.rt(60)
    u.fd(profundidad/2)
    u.rt(30)
    u.fd(base/2)
    uxref=u.xcor()
    uyref=u.ycor()
    u.pendown()
    u.goto(0,0)
    u.penup()
    u.goto(uxref,uyref)
    u.pendown()
    u.goto(base,0)
    u.penup()
    u.goto(uxref,uyref)
    u.pendown()
    u.goto(txref,tyref)
    u.penup()
    u.goto(uxref,uyref)
    u.pendown()
    u.goto(txref+base,tyref)
    t.hideturtle()
    u.hideturtle()
    r.hideturtle()
    
DibujarEje()    #Eje X
DibujarEje()    #Eje Y
t.lt(30)
DibujarEje()    #Eje Z
t.lt(60)       #Reubico eje X
u.lt(90)        #Reubico eje Y
r.lt(30)       #Reubico eje Z

t.color("red")
u.color("green")
r.color("blue")

graf=str(input("Ingrese nombre de lo que desea graficar: "))

if graf=="cubo":
##    base=int(input("Ingrese base: "))
##    altura=int(input("Ingrese altura: "))
##    profundidad=int(input("Ingrese profundidad: "))
##    ancho=int(input("Ingrese ancho de linea: "))
    CrearCubo(35,90,50,3)

elif graf=="cilindro":
##    radio=int(input("Ingrese radio: "))
##    profundidad=int(input("Ingrese profundidad: "))
##    ancho=int(input("Ingrese ancho de linea: "))
    CrearCilindro(75,200,3)

elif graf=="piramide":
    base=int(input("Ingrese base: "))
    altura=int(input("Ingrese altura: "))
    profundidad=int(input("Ingrese profundidad: "))
    ancho=int(input("Ingrese ancho de linea: "))
    CrearPiramide(base,altura,profundidad,ancho)
