import numpy as np
def sinSegmentacion(i,tiempoEjecucion,cola,bloques,fetch,accesoMemoria,ejecucion,Retroescritura,actualizacionProcesador,cantidadInstrucciones):
    for i in range(cantidadInstrucciones):
        cola.append(fetch)
        cola.append(accesoMemoria)
        cola.append(ejecucion)
        cola.append(Retroescritura)
        cola.append(actualizacionProcesador)
        for j in range(bloques):
            tiempoEjecucion += cola.pop(0)
    print('El tiempo de ejecucion fue: ', tiempoEjecucion)

def conSegmentacion(i,tiempoEjecucion,cola,bloques,fetch,accesoMemoria,ejecucion,Retroescritura,actualizacionProcesador,cantidadInstrucciones):

    memory = []
    primeraUnidad = []
    segundaUnidad = []
    terceraUnidad = []
    tiempoEjecucion = 0

    for i in range(cantidadInstrucciones):
        memory.append(fetch)
        memory.append(accesoMemoria)
        memory.append(ejecucion)
        memory.append(Retroescritura)
        memory.append(actualizacionProcesador)
        controlador = 1
    while len(memory) != 0:
        if controlador == 1:
            primeraUnidad.append(memory.pop(0))
            controlador = 2
        elif controlador == 2:
            segundaUnidad.append(memory.pop(0))
            controlador = 3
        elif controlador == 3:
            terceraUnidad.append(memory.pop(0))
            controlador = 1
    tiempoEjecucion = ((sum(primeraUnidad) + sum(segundaUnidad) + sum(terceraUnidad)) / 3)
    print('El tiempo de ejecucion fue: ', tiempoEjecucion)