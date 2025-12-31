from flask import Flask
from flask_login import LoginManager
from controllers.auth_controller import auth_bp
from controllers.calendar_controller import calendar_bp
from models.user import get_user_by_id   # ✅ IMPORT FIX

app = Flask(__name__)
app.secret_key = "advanced_calendar_secret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


app.register_blueprint(auth_bp)
app.register_blueprint(calendar_bp)

if __name__ == "__main__":
    app.run(debug=True)
