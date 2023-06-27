from flask import Flask, render_template, redirect, url_for, flash, request
from app.forms import AddRecipeForm
from app.model import db, Recipe


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

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
    
    @app.route('/recipe/delete/<int:id>')
    def recipe_delete(id):
        recipe = Recipe.query.get_or_404(id)
        try:
            db.session.delete(recipe)
            db.session.commit()
            flash('Рецепт удален!')
            return redirect('/')
        except:
            return 'При удалении рецепта произошла ошибка'
    
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


    return app