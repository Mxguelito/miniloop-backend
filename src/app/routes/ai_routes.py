from flask import Blueprint, render_template, request
from src.app.ai.ai_service import AIService

ai = Blueprint("ai", __name__)


@ai.route("/ia", methods=["GET", "POST"])
def inteligencia_artificial():

    resultado = None

    if request.method == "POST":

        data = {
            "departamentos": request.form.get("departamentos"),
            "deudas": request.form.get("deudas"),
            "reclamos": request.form.get("reclamos"),
            "incidentes": request.form.get("incidentes")
        }

        resultado = AIService.analizar_consorcio(data)

    return render_template(
        "ia.html",
        resultado=resultado
    )