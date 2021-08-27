
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if(edad >= 18):
        id = str(input("¿Tienes identificación oficial? (s/n): "))
        if (id == 's'):
            print('Trámite de licencia concedido')
        elif (id == 'n'): 
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    elif(0< edad <18):
        print('No cumples requisitos')
    else:
        print('Respuesta incorrecta')

if __name__ == '__main__':
    main()
