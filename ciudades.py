import pandas as pd

# Crear el diccionario con los datos iniciales
datos = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0]
}

# Crear el DataFrame usando el diccionario
df = pd.DataFrame(datos)

# Añadir la nueva columna 'Ciudad'
df['Ciudad'] = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']

# Mostrar el DataFrame actualizado
print("DataFrame actualizado con la columna 'Ciudad':")
print(df)
