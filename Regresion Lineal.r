# Usamos el dataset 'cars' que viene en R
modelo <- lm(dist ~ speed, data = cars)
summary(modelo) # Muestra las estadísticas del modelo