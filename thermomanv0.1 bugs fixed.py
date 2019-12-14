#thermoman v0.1
#by sovietic wolf 
#para la ayuda en termodinamica
#mande in 10/11/2019
def interpolacion():
    print("elegiste interpolar medidas")
    print("introduce las medidas X \n la incognita introducela como \"m\" \n las incognitas van en X")
    k1=(input("introduce X1>>>"))
    k2=(input("introduce X2>>>"))
    k3=(input("introduce X3>>>"))
    l1=(input("introduce y1>>>"))
    l2=(input("introduce y2>>>"))
    l3=(input("introduce y3>>>"))
    if(k1=="m"):
        a1=(float(l1))
        a2=(float(l2))
        a3=(float(l3))
        b2=(float(k2))
        b3=(float(k3))
        deltaL=(a1-b2)
        deltaX=(b2-b3)
        deltaL2=(a2-a3)
        m=((deltaL*deltaX)/deltaL2)+b2
        print("x \t y")
        print(m,"\t",l1)
        print(k2,"\t",l2)
        print(k3,"\t",l3)
        print("la m es de:",m)
        print(" ha ocurrido un error \n intentar otra vez?")
        print("y \" n")
        seleccion=input(">>>")
        if(seleccion=="y"):
            interpolacion()
        else:
            print("adios")
        
    elif(k2=="m"):
        a1=(float(l1))
        a2=(float(l2))
        a3=(float(l3))
        b1=(float(k1))
        b3=(float(k3))
        deltaL=(a1-a2)
        deltaL2=(a2-a3)
        deltaL3=(a1-a3)
        m=((b3*(deltaL)+b1*(deltaL2))/deltaL3)
        print("x \t y")
        print(k1,"\t",l1)
        print(m,"\t",l2)
        print(k3,"\t",l3)
        print("la m es de:",m)
        print(" ha ocurrido un error \n intentar otra vez?")
        print("y \" n")
        seleccion=input(">>>")
        if(seleccion=="y"):
            interpolacion()
        else:
            print("adios")


    elif(k3=="m"):
        a1=(float(l1))
        a2=(float(l2))
        a3=(float(l3))
        b1=(float(k1))
        b2=(float(k2))
        deltaL=(a1-a2)
        deltaL2=(a2-a3)
        m=b2-(((b1-b2)*(deltaL2))/deltaL)
        print("x \t y")
        print(k1,"\t",l1)
        print(k2,"\t",l2)
        print(m,"\t",l3)
        print("la m es de:",m)
        print(" ha ocurrido un error \n intentar otra vez?")
        print("y \" n")
        seleccion=input(">>>")
        if(seleccion=="y"):
            interpolacion()
        else:
            print("adios")
    else:
        print(" ha ocurrido un error \n intentar otra vez?")
        print("y \" n")
        seleccion=input(">>>")
        if(seleccion=="y"):
            interpolacion()
        else:
            print("adios")

print("bienvenido a el programa thermoman v0.1")
print(" hecho y diseñado por sovietic wolf ")
print("hecho en 10/11/2019")
print("funciones disponibles por el momento")
print("-interpolacion manual (1)")
select=input(">>>")
if (select=="1"):
    interpolacion()
else:
    print("bai")
