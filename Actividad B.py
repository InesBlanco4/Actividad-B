# Ines Blanco
# Division 117

#Actividad 7

def calcular_ventas_nacionales_con_iva(ventas_nacionales, iva):
    ventas_con_iva = ventas_nacionales * (1 + (iva / 100))
    return ventas_con_iva

def calcular_ventas_exportaciones_con_retencion(exportaciones, retencion):
    exportaciones_con_retencion = exportaciones * (1 + (retencion / 100))
    return exportaciones_con_retencion

def calcular_valor_total_ventas(ventas_nacionales, exportaciones, iva, retencion):
    ventas_nacionales_con_iva = calcular_ventas_nacionales_con_iva(ventas_nacionales, iva)
    exportaciones_con_retencion = calcular_ventas_exportaciones_con_retencion(exportaciones, retencion)
    valor_total = ventas_nacionales_con_iva + exportaciones_con_retencion
    return valor_total

#Actividad 8

def calcular_salario_total(horas_trabajadas, antiguedad_en_años):
    salario_total = horas_trabajadas * 10 * (1 + (antiguedad_en_años * 0.03))
    return salario_total


def calcular_productividad(artefactos_producidos, horas_trabajadas):
    productividad = artefactos_producidos / horas_trabajadas
    return productividad


def generar_reporte(nombre, edad, salario_total, productividad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario total: {salario_total}")
    print(f"Productividad: {productividad}")