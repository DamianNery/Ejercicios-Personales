#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Probando Tkinter y Prueba con sqlite3

import tkinter as tk
import sqlite3
import os

adminuser="admin"
adminpassw="1111"
global listauser
listauser=["damian"]
listapassw=["2222"]
listamateria=["Analisis Matematico","Algebra","Informatica","Fisica"]
listaexamen=["Parcial 1","Parcial 2","Recuperatorio","Final"]

#---VENTANA PPAL (INICIO PROGRAMA)---
def VentanaPpal():
    global ppal
    ppal=tk.Tk() #Ventana principal
    ppal.title("Mezcla tkinter y SQLite") #Titulo de la ventana
    ppal.config(bg="blue") #Color del fondo de la ventana
    ppal.geometry("600x400") # Tamaño de la ventana
    l1=tk.Label(bg="blue",fg="white",text="Usuario y Contraseña", width=20).pack()
    m1=tk.Message(bg="blue",fg="yellow",text="\nIngrese su nombre", width=300).pack()
    global e1
    e1=tk.Entry()
    e1.pack()
    m2=tk.Message(bg="blue",fg="yellow",text="\nIngrese su contraseña", width=300).pack()
    global e2
    e2=tk.Entry(show="*",width=4)
    e2.pack()
    b1=tk.Button(text="INGRESAR",command=IniciarSesion).pack(pady=30)
    ppal.mainloop() #Evento que llama al inicio del programa
#---VENTANA PPAL (INICIO PROGRAMA)---
#---VENTANA SECUNDARIA---
def VentanaSecu():
    global secu
    secu=tk.Toplevel(ppal) # Crea una ventana hija
    secu.config(bg="black") #Fondo ventana hija
    secu.geometry("450x400") #Tamaño ventana hija
    l2=tk.Label(secu,bg="black",fg="white",text="Aplicacion", width=15).pack()
    secu.withdraw() # oculta secu
#---VENTANA SECUNDARIA---
#---VENTANA TERCERA---
def VentanaTri():
    global tri
    tri=tk.Toplevel(secu) # Crea una ventana hija
    tri.config(bg="grey") #Fondo ventana hija
    tri.geometry("350x400") #Tamaño ventana hija
    tri.withdraw() # oculta secu
#---VENTANA TERCERA---
#---CHECK USER Y PASS---
def IniciarSesion():
    ppal.withdraw()
    VentanaSecu()
    global user
    global passw
    user=str(e1.get())
    passw=str(e2.get())
    if user==adminuser and passw==adminpassw:
        secu.deiconify() #Muestra secu
        AbrirDB()
        b2=tk.Button(secu,text="NUEVO USUARIO",width=15,command=CrearUser).pack(pady=5)
        b3=tk.Button(secu,text="ELIMINAR USUARIO",width=15,command=BorrarUser).pack(pady=5)
        b4=tk.Button(secu,text="NOTAS",width=15,command=CargarNotas).pack(pady=5)
        b5=tk.Button(secu,text="CERRAR SESION",width=15,command=CerrarSesion).pack(pady=5)
    elif user in listauser and passw in listapassw:
        secu.deiconify() #Muestra secu
        AbrirDB()
        b2=tk.Button(secu,text="VER NOTAS",command=VerNotas).pack(pady=5)
        b3=tk.Button(secu,text="CERRAR SESION",command=CerrarSesion).pack(pady=10)
    elif user not in listauser or passw not in listapassw:
        tk.messagebox.showerror(title="ERROR",
        message="USUARIO O CONTRASEÑA INCORRECTA")
        e1.delete(first=0,last=20)
        e2.delete(first=0,last=20)
        ppal.deiconify()
#---CHECK USER Y PASS---
#---CREAR USUARIO---
def CrearUser():
    secu.withdraw()
    VentanaTri()
    tri.deiconify()
    l3=tk.Label(tri,bg="grey",fg="black",text="\nCREAR USUARIO", width=20).pack()
    m3=tk.Message(tri,bg="grey",fg="black",text="\nIngrese su nombre", width=300).pack()
    global e3
    e3=tk.Entry(tri)
    e3.pack()
    m4=tk.Message(tri,bg="grey",fg="black",text="\nIngrese su contraseña", width=300).pack()
    global e4
    e4=tk.Entry(tri,show="*",width=4)
    e4.pack()
    b6=tk.Button(tri,text="CREAR",width=10,command=CrearEnLista).pack(pady=10)
    b8=tk.Button(tri,text="VOLVER",width=10,command=VolverSecu).pack()
#---CREAR USUARIO---
#---CREAR EN LA LISTA---
def CrearEnLista():
    if len(e4.get())==4:
        listauser.append(e3.get())
        listapassw.append(e4.get())
        tk.messagebox.showinfo(title="USUARIO",message="USUARIO CREADO")
    else:
        tk.messagebox.showerror(title="USUARIO",message="CONTRASEÑA INVALIDA")
    e3.delete(first=0,last=20)
    e4.delete(first=0,last=20)
    tri.withdraw()
    IniciarSesion()
#---CREAR EN LA LISTA---
#---BORRAR USUARIO---
def BorrarUser():
    secu.withdraw()
    VentanaTri()
    tri.deiconify()
    l3=tk.Label(tri,fg="black",bg="grey",text="\nBORRAR USUARIO", width=20).pack()
    m3=tk.Message(tri,fg="black",bg="grey",text="\nIngrese nombre a borrar", width=300).pack()
    global e5
    e5=tk.Entry(tri)
    e5.pack()
    m4=tk.Message(tri,fg="black",bg="grey",text="\nIngrese contraseña de administrador", width=300).pack()
    global e6
    e6=tk.Entry(tri,show="*",width=4)
    e6.pack()
    b6=tk.Button(tri,text="BORRAR",width=10,command=BorrarDeLista).pack(pady=10)
    b8=tk.Button(tri,text="VOLVER",width=10,command=VolverSecu).pack()
#---BORRAR USUARIO---
#---BORRAR DE LA LISTA---
def BorrarDeLista():
    print(e5.get())
    print(e6.get())
    if e5.get() in listauser:
        if e6.get()==adminpassw:
            pos=listauser.index(e5.get())
            listauser.remove(e5.get())
            print(listauser)
            listapassw.pop(pos)
            print(listapassw)
            tk.messagebox.showinfo(title="USUARIO",message="USUARIO BORRADO")
        else:
            tk.messagebox.showerror(title="USUARIO",message="CONTRASEÑA INCORRECTA")
    else:
        tk.messagebox.showerror(title="USUARIO",message="NO EXISTE EL USUARIO")
    e3.delete(first=0,last=20)
    e4.delete(first=0,last=20)
    tri.withdraw()
    IniciarSesion()
#---BORRAR DE LA LISTA---
#---CARGAR NOTAS---
def CargarNotas():
    secu.withdraw()
    VentanaTri()
    tri.deiconify()
    l4=tk.Label(tri,bg="grey",fg="black",text="NOTAS", width=15).pack()
    AbrirDB()
    global examen
    global materia
    global alumno
    examen=tk.StringVar()
    materia=tk.StringVar()
    alumno=tk.StringVar()
    l6=tk.Label(tri,bg="grey",fg="black",text="\nAlumno", width=20).pack()
    om3 = tk.OptionMenu(tri,alumno,*listauser).pack()
    l7=tk.Label(tri,bg="grey",fg="black",text="\nExamen", width=20).pack()
    om1 = tk.OptionMenu(tri,examen,*listaexamen).pack()
    l5=tk.Label(tri,bg="grey",fg="black",text="\nMateria", width=20).pack()
    om2 = tk.OptionMenu(tri,materia,*listamateria).pack()
    global nota
    l8=tk.Label(tri,bg="grey",fg="black",text="\nNota", width=10).pack()
    nota=tk.Entry(tri,width=5)
    nota.pack()
    b7=tk.Button(tri,text="IMPRIMIR",width=10,command=Cargar).pack(pady=10)
    b8=tk.Button(tri,text="VOLVER",width=10,command=VolverSecu).pack()

def Cargar():
    print(examen.get(),materia.get(),alumno.get(),nota.get())
    InsertarDB()
    tri.withdraw()
    IniciarSesion()
#---CARGAR NOTAS---
#---VER NOTAS---
def VerNotas():
    global connection
    connection = sqlite3.connect("notas.db") #Creo database llamada notas
    global cursor
    cursor = connection.cursor()

    f=open("notas.csv","w")
    f.write("nombre;materia;examen;nota\n")
    
    sql_command = """ SELECT * FROM notas WHERE usuario == ? """
    cursor.execute(sql_command,(user,))
    
    data = cursor.fetchall()
    print("Data es: ",data)
    for row in data:
##        datanumero = row[0]
        datanombre = row[1]
        datamateria = row[2]
        dataexamen = row[3]
        datanota = row[4]
        # Now print fetched result
        print ("nombre=%s,materia=%s,examen=%s,nota=%s" %
          (datanombre, datamateria, dataexamen, datanota))
        f.write((datanombre+";"+datamateria+";"+dataexamen+";"+datanota+"\n"))
    f.close()
    os.system("libreoffice notas.csv")
    
#---VER NOTAS---
#---CERRAR SESION---
def CerrarSesion():
    secu.withdraw()
    ppal.deiconify()
    user=" "
    passw=" "
    e1.delete(first=0,last=20)
    e2.delete(first=0,last=20)
    connection.commit()
    connection.close() #Cerrar base de datos
#---CERRAR SESION---
#---VOLVER SECU---
def VolverSecu():
    tri.withdraw()
    secu.deiconify()
#---VOLVER SECU---
#---ABRIR BASE DE DATOS---
def AbrirDB():
    global connection
    connection = sqlite3.connect("notas.db") #Creo database llamada notas
    global cursor
    cursor = connection.cursor()

##    cursor.execute("""DROP TABLE notas;""") #Borrar tabla

    sql_command = """
    CREATE TABLE IF NOT EXISTS notas ( 
    staff_number INTEGER PRIMARY KEY,
    usuario VARCHAR(20), 
    materia VARCHAR(30), 
    examen VARCHAR(2), 
    nota VARCHAR(4));""" #Crear tabla
    cursor.execute(sql_command)
#---ABRIR BASE DE DATOS---
#---INSERTAR EN BASE DE DATOS---
def InsertarDB():
    sql_command = """INSERT INTO notas (
    staff_number, usuario, materia, examen, nota)
        VALUES (NULL, ?, ?, ?, ?);"""
    cursor.execute(sql_command,(alumno.get(),materia.get(),examen.get(),nota.get()))
    # never forget this, if you want the changes to be saved:
    connection.commit()
#---INSERTAR EN BASE DE DATOS---
#---USUARIOS Y CONTRAS---
def TablaUsers():
    sql_command = """
    CREATE TABLE IF NOT EXISTS users ( 
    staff_number INTEGER PRIMARY KEY,
    nombre VARCHAR(20), 
    password VARCHAR(30));""" #Crear tabla
    cursor.execute(sql_command)

VentanaPpal()
