#Fredy Omar Avila Triana - 01251151005
#Andres Felipe Castilla Caselles - 01251151011

#Numero flotante mayor al numero ingresado
def numero_float_mayor_igual_que(n1: float, texto: str):
    while True:
        try:
            input_numero = float(input(texto))
            if input_numero <= n1:
                print("Error: Ha ingresado un numero menor o igual a 0")
                continue
            return input_numero
        except ValueError:
            print("Error: ha ingresado un valor no numerico")

#Numero entero mayor al numero ingresado
def numero_int_mayor_que(n1: int, texto: str):
    while True:
        try:
            input_numero = int(input(texto))
            if input_numero < n1:
                print("Error: Ha ingresado un numero menor o igual a 0")
                continue
            return input_numero
        except ValueError:
            print("Error: ha ingresado un valor no numerico")

#Calcular la tasa_mensual (tm: tasa mensual)
def tasa_mensual(plazo_mensual: int):
    ecuacion_tm = 0.001695 * plazo_mensual + 0.0983
    return ecuacion_tm

#Calcular la liquidacion_mensual retorna en lista para el guardado de datos
def liquidacion_mensual(tasa: float, saldo_inicial: float, plazo_mensual: int):
    list_liquidacion = []
    for i in range(plazo_mensual):
        pass

#Recoleccion datos CDT
input_moton_inicial = numero_float_mayor_igual_que(0,"Ingrese el monto inicial: ")
input_plazo_mensual = numero_int_mayor_que(0,"Ingrese el plazo en meses: ")