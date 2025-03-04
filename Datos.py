from dbfread import DBF
import pandas as pd

# Ruta del archivo DBF
file_path = "ruta\\del\\arhivo"  # Cambia esto por la ruta real

# Leer el archivo DBF y convertirlo en un DataFrame
dbf_table = DBF(file_path, load=True)
df = pd.DataFrame(iter(dbf_table))

# Mostrar las primeras filas
print(df.head())

# Guardar como CSV si necesitas exportarlo
df.to_csv("archivo_convertido.csv", index=False, encoding="utf-8")