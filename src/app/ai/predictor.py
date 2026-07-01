import joblib

# Cargar el modelo entrenado
modelo = joblib.load("src/app/ai/modelo.joblib")


def predecir_prioridad(departamentos, deudas, reclamos, incidentes):
    resultado = modelo.predict([
        [departamentos, deudas, reclamos, incidentes]
    ])

    return int(resultado[0])