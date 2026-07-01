import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Cargar dataset
df = pd.read_csv("src/app/ai/dataset.csv")

# Variables de entrada
X = df[["departamentos", "deudas", "reclamos", "incidentes"]]
#variable objetivo
y = df["prioridad"]

# Crear modelo
modelo = LogisticRegression()

# Entrenar
modelo.fit(X, y)

# Guardar modelo
joblib.dump(modelo, "src/app/ai/modelo.joblib")

print("Modelo entrenado correctamente.")