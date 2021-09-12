import Categoria1
import Categoria2
import Categoria3
import Categoria4
import Categoria5
import Configurar


i=0
while (i<1):
    print('Bienvenido a nuestro juego Preguntas y Respuesas!')
    print('¿Antes de emprezar deseas agregar una pregunta al banco de preguntas? -->  Si (s), No (n)')
    config=input()
    if(config=='s'):
     Configurar.Configuracion()
    print('¿Quieres agregar otra pregunta?  -->  Si (s), No (n)')
    Res=input()
    if(Res=='s'):
        c=1;
    else:
        print('Juego patrocinado por Challenge Sofka 2021!!')
        print('En breve empezamos!')
        print('Loading......')
        print('Empieza el juego!!')
        Decision=''
        Premio = 0
        PremioAcumulado = 0
        print('Ingresa tu nickname:   ')
        Nombre=input()
        Premio,Decision=Categoria1.Pregunta(Nombre, Premio)
        if(Premio==0 or Decision=='s'):
            c=1
            print('Fin del juego :( ')
        else:
            Premio,Decision=Categoria2.Pregunta2(Nombre, Premio)
            if(Premio==0 or Decision=='s'):
                c=1
                print('Fin del juego :( ')
            else:
                Premio,Decision=Categoria3.Pregunta3(Nombre, Premio)
                if(Premio==0 or Decision=='s'):
                    c=1
                    print('Fin del juego :( ')
                else:
                    Premio,Decision=Categoria4.Pregunta4(Nombre, Premio)
                    if(Premio==0 or Decision=='s'):
                        c=1
                        print('Fin del juego :( ')
                    else:
                        Premio,Decision=Categoria5.Pregunta5(Nombre, Premio)
                        if(Premio==0 or Decision=='s'):
                            c=1

