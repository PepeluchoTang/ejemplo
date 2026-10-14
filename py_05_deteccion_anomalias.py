# 5. Detección de Anomalías (Análisis de Outliers)
import pandas as pd
import numpy as np

# E - Extracción (Volumen de peticiones de red por minuto)
data = {'Peticiones_Red': [120, 125, 118, 130, 122, 120, 950, 128, 115, 121, 124, 15]}
df = pd.DataFrame(data)

# T - Transformación / Filtro Estadístico de Z-Score
# Identificar registros fuera de 2 desviaciones estándar de la media
media = df['Peticiones_Red'].mean()
desviacion = df['Peticiones_Red'].std()

df['Z_Score'] = (df['Peticiones_Red'] - media) / desviacion
df['Es_Anomalia'] = df['Z_Score'].abs() > 2.0

# L - Carga / Alertas
anomalias = df[df['Es_Anomalia'] == True]
print(f"Media del tráfico normal: {media:.2f}")
print("
=== AMENAZAS O ANOMALÍAS DETECTADAS ===")
print(anomalias)
