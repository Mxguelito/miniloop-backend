from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "MiniLoop Backend Running"

@main.route("/health")
def health():
    return {
        "status": "ok",
        "message": "MiniLoop API Running"
    }