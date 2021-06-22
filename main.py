from msg.msgforuser import main_menssage, intructions_indications
from processcomputing.procesador import procesador

if __name__ == '__main__':
    option=0
    while option !=3:
        main_menssage()
        option = int(input('Digite una opcion: '))
        if option==1:
            intructions_indications()
            option=int(input())
            if option==1:
                procesador(1,1000)
            elif option==2:
                procesador(1,5000)
            elif option==3:
                procesador(1,10000)
            else:
                pass
        elif option==2:
            intructions_indications()
            option = int(input())
            if option == 1:
                procesador(2,1000)
            elif option == 2:
                procesador(2,5000)
            elif option == 3:
                procesador(2,10000)
            else:
                pass
