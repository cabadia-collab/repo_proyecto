#Programa Principal 


from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_minimo_senal
from src.metricas import calcular_maximo_senal
from src.metricas import calcular_promedio_senal

datos= cargar_datos("datos/PulseLab_mock_data.csv")

datos_validos= []

for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)

promedio= calcular_promedio_senal(datos_validos)
minimo= calcular_minimo_senal(datos_validos)
maximo= calcular_maximo_senal(datos_validos)

resultado= (promedio, minimo, maximo)

print(resultado)