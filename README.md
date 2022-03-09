# Proyecto Simulación La Cocina de Kojo

## Yansaro Rodriguez Paez C412

### Problema

La cocina de Kojo es uno de los puestos de comida rapida en un centro comercial. El centro comercial esta abierto entre las 10:00 am y las 9:00 pm cada dia. En este lugar se sirven dos tipos de productos: sandwiches y sushi. Para los objetivos de este proyecto se asumira que existen solo dos tipos de consumidores: unos consumen solo sandwiches y los otros consumen solo productos de la gama del sushi. En Kojo hay dos periodos de hora pico durante un dıa de trabajo; uno entre las 11:30 am y la 1:30 pm, y el otro entre las 5:00 pm y las 7:00 pm. El intervalo de tiempo entre el arribo de un consumidor y el de otro no es homogeneo pero, por conveniencia, se asumira que es homogeneo. El intervalo de tiempo de los segmentos homogeneos, distribuye de forma exponencial. Actualmente dos empleados trabajan todo el dıa preparando sandwiches y sushi para los consumidores. El tiempo de preparacion depende del producto en cuestion. Estos distribuyen de forma unie, en un rango de 3 a 5 minutos para la preparacion de sandwiches y entre 5 y 8 minutos para la preparacion de sushi. El administrador de Kojo esta muy feliz con el negocio, pero ha estado recibiendo quejas de los consumidores por la demora de sus peticiones. El esta interesado en explorar algunas opciones de distribucion del personal para reducir el numero de quejas. Su interes esta centrado en comparar la situacion actual con una opcion alternativa donde se emplea un tercer empleado durante los periodos mas ocupados. La medida del desempeno de estas opciones estara dada por el porciento de consumidores que espera mas de 5 minutos por un servicio durante el curso de un dıa de trabajo. Se desea obtener el porciento de consumidores que esperan mas de 5 minutos cuando solo dos empleados estan trabajando y este mismo dato agregando un empleado en las horas pico.

### Solución

Para visualizar la solución, ejecute el programa `main.py` en el cual se ejecutan 2 simulaciones, uno por cada cantidad de empleados especificada. El resultado refleja la cantidad de comensales atendidos contra el porcentaje de comensales que demoraron más de 5 minutos en la cola.

En dicha solución, definiremos 4 variales principales:

- cola cuando un cliente llega a la tienda
- tiempo que demora un cliente en ser atendido en dependencia de su orden (sushi o sandwich)
- estado de un empleado en un momento puntal
- tiempo total de atención a cada cliente en forma de lista

### Modelación

El estado inicial del problema será el siguiente:

- trab_ocupados(i) = no_ocupado (False)
- t = 0
- espera = []
- llegada = []
- t_llegada = expon()
- t_total = t_llegada

Si un cliente llega:

- generamos los tiempos de llegada, agregando al 3er trabajador en caso necesario
- t_total = t_llegada
- si algún trabajador esta libre atiende al nuevo comensal

Al empleado i empleado terminar de atender a un comensal:

- trab_ocupados(i) = False
- t = llegada.dequeue()
- t_total = min(llegada,espera)
- espera.append(t_total - t)
- t_pedido = gen_t(sand_o_sush)
  
Si no podemos seguir trabajando porque la tienda cerró y no hay más clientes en cola:

- termina el proceso

### Consideraciones

Como era de esperar, tener 1 trabajador extra ayuda a que los comensales disfruten sus platos más rápido. Aún asi, es cierto que la diferencia no es tan grande teniendo en cuenta que en la mayoría de las iteraciones ejecutadas, la diferencia era en promedio de un 10%.

## Link del código en github

<https://github.com/yarn-rp/simulacion_cocina_kojo>
