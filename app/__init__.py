from flask import Flask, render_template, redirect

from app.model import db, Recipe


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    @app.route('/home')
    def index():
        recipes_list = Recipe.query.order_by(Recipe.created_at.desc()).all()
        return render_template('index.html', recipes_list=recipes_list)
    
    return app