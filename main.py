#Programa Principal 


from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_metricas

datos= cargar_datos("datos/datos_proyecto.csv")

datos_validos= []

for registro in datos:
    if validar_registro(registro):
        datos_validos.append(registro)

resultado= calcular_metricas(datos_validos)

print(resultado)