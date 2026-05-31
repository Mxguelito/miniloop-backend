from flask import request, jsonify

from src.app.services.auth_service import AuthService


class AuthController:

    @staticmethod
    def register():

        data = request.get_json()

        response = AuthService.register(data)

        return jsonify(response["body"]), response["status"]

    @staticmethod
    def login():

        data = request.get_json()

        response = AuthService.login(data)

        return jsonify(response["body"]), response["status"]
    
       
    @staticmethod
    def logout(current_user):

        response = AuthService.logout(current_user)

        return jsonify(response["body"]), response["status"]


    @staticmethod
    def profile(current_user):

        return jsonify({
            "success": True,
            "user": current_user.to_dict()
        }), 200
    

    @staticmethod
    def dashboard(current_user):

        response = AuthService.dashboard(current_user)

        return jsonify(response["body"]), response["status"]
    

    @staticmethod
    def update_profile(current_user):

        response = AuthService.update_profile(
            current_user,
            request.get_json()
        )

        return jsonify(response["body"]), response["status"]
    

    @staticmethod
    def validate_session(current_user):

        response = AuthService.validate_session(current_user)

        return jsonify(response["body"]), response["status"]