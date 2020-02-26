# -*- coding: utf-8 -*-

from VALID import ns, OKI
import calendar

def AB(n): #VALIDAR DATO DE ENTRADA OPCIÓN (A/B)
    while n!=("A") and n!=("B"):
        n=input("Escriba solo \'A\' o \'B\' segun su opción: ")
    return n

def anno_valido(n): #VALIDAR DATO DE ENTRADA (AÑO)
    while n<1 or n>9999:
        n=OKI(input("Introduzca un año valido: "))
    return n

def mes_valido(n): #VALIDAR DATO DE ENTRADA (MES)
     while n<1 or n>12:
         n=OKI(input("Introduzca un mes valido: "))
     return n


while True:
    print("\n------------------------------CALENDARIOS------------------------------\n")
    print("""Escoja una opción:
A)Ver los calendarios correspondientes a un determinado año.
B)Ver el calendario correspondiente a un año y mes determinados.
""")
    opcion=AB(input("Introduzca su opción(A/B): "))
    if opcion==("A"):
        anno=anno_valido(OKI(input("Introduce el año cuyos calendarios desea ver: ")))
        cl=calendar.TextCalendar()
        calendario=cl.formatyear(anno)
    else:
        anno=anno_valido(OKI(input("Introduzca el año: ")))
        mes=mes_valido(OKI(input("Introduzca mes: ")))
        cl=calendar.TextCalendar()
        calendario=cl.formatmonth(anno,mes)
    print("\n"+calendario)
        
    conti=ns(input("¿Desea continuar?(n/s): "))
    if conti==("n"):
        break
