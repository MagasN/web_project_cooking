from flask import Flask, render_template, redirect
from app.model import db, Recipe


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    @app.route('/home')
    def index():
        # Нужно доделать вывод автора рецепта, дату и т.п.
        recipes_list = Recipe.query.order_by(Recipe.created_at.desc()).all()
        return render_template('index.html', recipes_list=recipes_list)

    @app.route('/recipes/top')
    def top_recipes():
        # Нужно доделать вывод автора рецепта, дату и т.п.
        recipes_list = Recipe.query.order_by(Recipe.positive_feedback.desc()).all()
        return render_template('top_recipes.html', recipes_list=recipes_list)
    
    @app.route('/recipes/add')
    def add_recipe():
        # Нужно доделать, сделал простенькую форму с самыми основными полями для начала
        return render_template('add_recipe.html')
    

    return app