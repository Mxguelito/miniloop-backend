import bcrypt
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "miniloop_ultra_secret_jwt_key_2026_backend_enterprise"


# =========================
# HASH PASSWORD
# =========================
def hash_password(password):
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return hashed.decode("utf-8")


# =========================
# VERIFY PASSWORD
# =========================
def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


# =========================
# GENERATE JWT TOKEN
# =========================
def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token