
from numpy import Infinity

from simulacion.util import uni

def hora_pico(t: float) -> bool:
    intervalo_1 = (90*60, 90*60 + 150*60)
    intervalo_2 = (7*60*60, 7*60*60 + 120*60)
    return (t > intervalo_1[0] and t < intervalo_1[1]) or (t > intervalo_2[0] and t < intervalo_2[1])


def genera_cliente(i, espera, t_total, llegada, t_trabajo):
    espera.append(t_total - llegada.pop(0))
    sand_o_sushi = False if uni(
        0, 1) < 0.5 else True
    if sand_o_sushi:
        t_trabajo[i] = t_total + uni(5, 8) * 60
    else:
        t_trabajo[i] = t_total + uni(3, 5) * 60