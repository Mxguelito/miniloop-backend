from flask import Blueprint,render_template, request, redirect, url_for, session, flash,make_response
from src.app.shared.middleware.auth_middleware import token_required
from src.app.auth.services.auth_service import AuthService
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")


@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        data = {
            "email": request.form.get("correo"),
            "password": request.form.get("password")
        }

        response = AuthService.login(data)

        if response["status"] == 200:
            access_token = response["body"]["token"]
            
            resp = make_response(redirect("/dashboard"))
            set_access_cookies(resp, access_token)
            return resp
        
        return render_template("login.html", error=response["body"]["message"])
    
    return render_template("login.html")
        
        


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        print("ENTRO A REGISTER")

        data = {
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "email": request.form.get("email"),
            "documento": request.form.get("documento"),
            "password": request.form.get("password")
        }

        print(data)

        response = AuthService.register(data)

        if response["status"]== 201:
            flash(response["body"]["message"], "success")
            return redirect(url_for("main.login"))
        
        flash(response["body"]["message"], "danger")

    return render_template("register.html")

@main.route("/dashboard")
@token_required  
def dashboard(current_user):

    response=AuthService.dashboard(current_user)

    if not response["body"]["success"]:
        return redirect("/login")
    
    return render_template("dashboard.html", dashboard=response["body"]["dashboard"])


@main.route("/profile")
@token_required
def profile(current_user):
    response = AuthService.profile(current_user)
    if not response["body"]["success"]:
        return redirect("/dashboard")
    
    return render_template("profile.html", profile=response["body"]["profile"])

@main.route("/profile/edit", methods=["GET", "POST"])
@token_required
def edit_profile(current_user):

    if request.method == "POST":

        data = {
            "nombre": request.form.get("nombre"),
            "apellido": request.form.get("apellido"),
            "telefono": request.form.get("telefono"),
        }

        response = AuthService.update_profile(current_user, data)

        if response["body"]["success"]:
            return redirect("/profile")

        return render_template(
            "edit_profile.html",
            error=response["body"]["message"],
            profile=data
        )

    response = AuthService.profile(current_user)

    return render_template(
        "edit_profile.html",
        profile=response["body"]["profile"]
    )

@main.route("/logout")
@token_required
def logout(current_user):
    AuthService.logout(current_user)
    resp = make_response(redirect(url_for("main.home")))
    unset_jwt_cookies(resp)
    session.clear()
    return resp

@main.route("/auditoria")
@token_required
def auditoria(current_user):

    response = AuthService.audit()

    return render_template(
        "auditoria.html",
        auditorias=response["body"]["auditorias"]
    )

@main.route("/roles")
def roles():
    return render_template("construccion.html")

@main.route("/permisos")
def permisos():
    return render_template("construccion.html")

@main.route("/construccion")
def construccion():
    return render_template("construccion.html")

@main.route("/health")
def health():
    return {
        "status": "ok",
        "message": "MiniLoop API Running"
    }