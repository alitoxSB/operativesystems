import time
import numpy as np
from processcomputing.unidadFuncional import sinSegmentacion, conSegmentacion


def procesador(option, cantidadInstrucciones):
    fetch = 5
    accesoMemoria = np.random.randint(10, 20)
    ejecucion = np.random.randint(20, 45)
    Retroescritura = np.random.randint(2, 5)
    actualizacionProcesador = 10
    i = 0
    tiempoEjecucion = 0
    cola = []
    bloques = 5

    if option==1:
        sinSegmentacion(i,tiempoEjecucion,cola,bloques,fetch,accesoMemoria,ejecucion,Retroescritura,actualizacionProcesador,cantidadInstrucciones)
    elif option==2:
        conSegmentacion(i,tiempoEjecucion,cola,bloques,fetch,accesoMemoria,ejecucion,Retroescritura,actualizacionProcesador,cantidadInstrucciones)





