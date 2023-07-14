from flask import Flask, render_template
from flask_login import LoginManager

from app.db import db
from app.config import Config

from app.recipe.models import Recipe
from app.user.models import User
from app.user.views import blueprint as user_bp
from app.recipe.views import blueprint as recipe_bp
from app.admin.views import blueprint as admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(admin_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        recipes_list = Recipe.query.order_by(Recipe.created_at.desc()).all()
        return render_template('index.html', recipes_list=recipes_list)

    return app