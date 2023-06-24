from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_required

from app.forms import AddRecipeForm
from app.model import db, Recipe

from app.model import User
# from app.user.model import User
from app.user.views import blueprint as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
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
        # Нужно доделать
        add_recipe_form = AddRecipeForm()
        return render_template('add_recipe.html', form=add_recipe_form)
    
    @app.route('/process-add-recipe', methods=['POST'])
    def process_add_recipe():
        form = AddRecipeForm()
        if form.validate_on_submit():
            new_recipe = Recipe(title=form.title.data,
                                decription_recipe=form.decription_recipe.data,
                                steps_recipe=form.steps_recipe.data,
                                servings=form.servings.data,
                                time_cooking=form.time_cooking.data
                                )
            db.session.add(new_recipe)
            db.session.commit()
            flash('Рецепт успешно добавлен!')
            return redirect(url_for('index'))
        flash('Неправильно заполнена форма!')
        return redirect(url_for('add_recipe'))
    
    @app.route('/search')
    def search():
        return render_template('search.html')
    
    @app.route('/search-results')
    def search_results():
        q = request.args.get('q')
        print(q)
        if q:
            search_results = Recipe.query.filter(Recipe.title.contains(q) | Recipe.decription_recipe.contains(q)).all()
            print(type(search_results))
        return render_template('search_result.html', search_results=search_results)

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ!'
        else:
            return 'Доступ закрыт.'

    return app