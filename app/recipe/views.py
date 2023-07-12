from flask import Blueprint, render_template, redirect, flash, url_for, request
import os
from werkzeug.utils import secure_filename
from app.recipe.forms import AddRecipeForm, EditRecipeForm
from app.recipe.models import Recipe
from app.db import db
from app.config import Config


blueprint = Blueprint('recipe', __name__, url_prefix='/recipes')

@blueprint.route('/top')
def top_recipes():
    recipes_list = Recipe.query.order_by(Recipe.positive_feedback.desc()).all()
    return render_template('top_recipes.html', recipes_list=recipes_list)
    
@blueprint.route('/<int:id>')
def recipe_page(id):
    recipe = Recipe.query.get(id)
    return render_template('recipe_page.html', recipe=recipe)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@blueprint.route('/add', methods=['POST', 'GET'])
def add_recipe():
    form = AddRecipeForm()
    if form.validate_on_submit() and request.method == 'POST':
        print(form.image_recipe.data)
        file = form.image_recipe.data
        filename = secure_filename(file.filename)
        if file:
            if allowed_file(filename):
                file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            else:
                flash('Разрешенные типы файлов - png, jpg, jpeg, gif. К сожалению рецепт не добавлен, попробуйте ещё раз.')
                return redirect(url_for('index'))
        new_recipe = Recipe(title=form.title.data,
                            image_recipe=filename,
                            decription_recipe=form.decription_recipe.data,
                            steps_recipe=form.steps_recipe.data,
                            servings=form.servings.data,
                            time_cooking=form.time_cooking.data
                            )
        try:
            db.session.add(new_recipe)
            db.session.commit()
            flash('Рецепт успешно добавлен!')
            return redirect(url_for('index'))
        except:
            return "При добавлении рецепта произошла ошибка"
    return render_template('add_recipe.html', form=form)
    
@blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.filter(Recipe.id==id).first()
    print(recipe)
    form = EditRecipeForm()
    if form.validate_on_submit() and request.method == 'POST':
        print(form.image_recipe.data)
        form.populate_obj(recipe)
        try:
            db.session.commit()
            flash('Рецепт успешно обновлён!')
            return redirect('/')
        except:
            return "При редактировании рецепта произошла ошибка"
    form = EditRecipeForm(obj=recipe)
    return render_template('edit_recipe.html', recipe=recipe, form=form)
    
@blueprint.route('/delete/<int:id>')
def recipe_delete(id):
    recipe = Recipe.query.get_or_404(id)
    try:
        db.session.delete(recipe)
        db.session.commit()
        flash('Рецепт удален!')
        return redirect('/')
    except:
        return 'При удалении рецепта произошла ошибка'
        
@blueprint.route('/search')
def search():
        return render_template('search.html')
    
@blueprint.route('/search-results')
def search_results():
    q = request.args.get('q')
    print(q)
    if q:
        search_results = Recipe.query.filter(Recipe.title.contains(q) | Recipe.decription_recipe.contains(q)).all()
        print(type(search_results))
    return render_template('search_result.html', search_results=search_results)
@blueprint.route('/favorite')
def recipes_favorites():
    return render_template('favorites_recipes.html')

@blueprint.route('/my')
def my_recipes():
    return render_template('my_recipes.html')
    