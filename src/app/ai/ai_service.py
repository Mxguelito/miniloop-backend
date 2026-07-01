from src.app.ai.predictor import predecir_prioridad


class AIService:

    @staticmethod
    def analizar_consorcio(data):

        departamentos = int(data.get("departamentos"))
        deudas = int(data.get("deudas"))
        reclamos = int(data.get("reclamos"))
        incidentes = int(data.get("incidentes"))

        resultado = predecir_prioridad(
            departamentos,
            deudas,
            reclamos,
            incidentes
        )

        motivos = []

        if deudas >= 5:
            motivos.append("Gran cantidad de deudas registradas.")

        if reclamos >= 5:
            motivos.append("Existen numerosos reclamos pendientes.")

        if incidentes >= 3:
            motivos.append("Se detectaron varios incidentes recientes.")

        if departamentos >= 50:
            motivos.append(
                "El consorcio posee muchas unidades, aumentando la complejidad administrativa."
            )

        if resultado == 0:

            prioridad = "BAJA"
            color = "success"

            descripcion = (
                "El consorcio presenta un nivel de riesgo bajo. "
                "No se requieren acciones inmediatas."
            )

        else:

            prioridad = "ALTA"
            color = "danger"

            descripcion = (
                "La Inteligencia Artificial recomienda revisar este consorcio con prioridad."
            )

        return {
            "prioridad": prioridad,
            "color": color,
            "descripcion": descripcion,
            "motivos": motivos
        }