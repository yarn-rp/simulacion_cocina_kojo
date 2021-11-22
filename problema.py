from simulacion.generadores import genera_cliente, hora_pico

from numpy import Infinity

from simulacion.util import expon

def problem(trab_adic):
    t_cierre = 11 * 60 * 60

    abierta = True
    t_total = 0

    trab_ocupados = [False, False]  
    t_de_trabajo = [Infinity, Infinity, Infinity]

    llegada = []

    espera = []

    t_llegada = expon(1/1024)

    while abierta or any(trab_ocupados):
        proximo_libre = min(t_de_trabajo)

        if t_llegada <= proximo_libre and t_llegada < t_cierre:
            t_total = t_llegada
            llegada.append(t_total)

            if not all(trab_ocupados):
                i = trab_ocupados.index(False)
                trab_ocupados[i] = True

                genera_cliente(
                    i, espera, t_total, llegada, t_de_trabajo)

            if hora_pico(t_total):
                t_llegada = t_total + expon(1/100)

                if trab_adic and len(trab_ocupados) == 2:
                    trab_ocupados.append(False)
            else:

                if len(trab_ocupados) == 3 and not trab_ocupados[2]:
                    trab_ocupados.pop()

                t_llegada = t_total + expon(1/1024)

        elif (t_llegada > proximo_libre) or (any(trab_ocupados) and not abierta):
            i = t_de_trabajo.index(proximo_libre)
            t_total = proximo_libre

            if len(llegada) > 0:
                genera_cliente(
                    i, espera, t_total, llegada, t_de_trabajo)
            else:
                trab_ocupados[i] = False
                t_de_trabajo[i] = Infinity

        if t_total >= t_cierre or t_llegada >= t_cierre:
            abierta = False

    return espera
