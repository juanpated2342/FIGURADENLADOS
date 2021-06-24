import turtle as t
from turtle import *
title("ALGORITMO DE N LADOS")
def main():
    # AQUI SE DEBE DE SELECIONAR EL ALGORITMO DESEADO BRESENHAMS O DDA
    tipo = int(input("ALGORITMOS..\n1.DDA \n2.Bresenhams \nSelecciona un algoritmo: "))

    # ALGORITMO DE DDA
    if tipo == 1: 
        x1=3
        x2=4
        y1=5
        y2=6
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        t.xlim=((x1-2,x2+2))
        t.ylim=((y1-2, y2+2))
        if (dx) > (dy):
            steps = (dx)
        else:
            steps = (dy)
            
        xInc = float(dx / steps)
        yInc = float(dy / steps)

        xInc = round(xInc,1)
        yInc = round(yInc,1)

        print("******ALGORITMO DDA******")
        n = int(input("\nIngresa el numero de lados de la figura:"))
        print("Tu numero de lados es ", n)
        angle = 180-(((n-2)/n)*180) # La suma de los ángulos internos del polígono de n lados se divide por n para obtener el valor del ángulo externo del polígono de n lados
        print("VALORES\n  X--------Y")

        for i in range(n):
            t.left(angle)
            t.fd(150)   
            dot(10,0,0,0)#SE DEBEN DE MARCAR LOS PUNTOS A CONOCER      
            p=t.pos ()
            print('\n'+str(p))

    #ALGORITMO DE BRESENHAMS
    if tipo == 2:
        x1=3
        x2=4
        y1=5
        y2=6
        t.xlim = ((x1-5, x2+5))
        t.ylim = ((y1-5, y2+5))
        x = x1
        y = y1
        dx = abs (x2 -x1)
        dy = abs (y2 - y1)
        p = 2*dy - dx

        while x <= x2:
            x+= 1
            if p < 0:
                p = p + 2 * dy
            else:
                p = p + (2*dy) - (2*dx)
                y+= 1
            print("******ALGORITMO BRESENHAMS******")
            n = int(input("\nIngresa el numero de lados de la figura:"))
            print("Tu numero de lados es ", n)
            angle = 180-(((n-2)/n)*180) # La suma de los ángulos internos del polígono de n lados se divide por n para obtener el valor del ángulo externo del polígono de n lados
            print("VALORES\n  X--------Y")
            for i in range(n):
                t.left(angle)
                t.fd(150)
                hideturtle()
                dot(10,0,0,0)#SE DEBEN DE MARCAR LOS PUNTOS A CONOCER  
                p=t.pos ()
                print('\n'+str(p))
    onkeypress(bye, 'q')  
    listen()
if __name__ == '__main__':
    main()
    onkeypress(bye, 'q')  
    listen()