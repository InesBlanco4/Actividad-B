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