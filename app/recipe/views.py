import os
from flask import abort, Blueprint, current_app, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from app.recipe.forms import AddRecipeForm, EditRecipeForm, CommentForm
from app.recipe.models import Comment, Recipe
from app.user.models import User
from app.db import db
from app.utils import get_redirect_target
from app.config import Config

blueprint = Blueprint('recipe', __name__, url_prefix='/recipes')

@blueprint.route('/top')
def top_recipes():
    recipes_list = Recipe.query.order_by(Recipe.positive_feedback.desc()).all()
    return render_template('top_recipes.html', recipes_list=recipes_list)
    
@blueprint.route('/<int:id>')
def recipe_page(id):
    recipe = Recipe.query.get(id)
    form = CommentForm(recipe_id = recipe.id)
    return render_template('recipe_page.html', recipe=recipe, comment_form=form)

@blueprint.route('/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        if Recipe.query.filter(Recipe.id == form.recipe_id.data).first():
            comment = Comment(comment=form.comment_text.data, recipe_id=form.recipe_id.data, user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            flash('Комментарий успешно добавлен') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash('Ошибка в заполнении поля "{}": - {}'.format(
                        getattr(form, field).label.text,
                        error
                    ))
        return redirect(get_redirect_target())  

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@blueprint.route('/add', methods=['POST', 'GET'])
def add_recipe():
    form = AddRecipeForm()
    if form.validate_on_submit() and request.method == 'POST':
        file = form.image_recipe.data
        filename = secure_filename(file.filename)
        if file:
            if allowed_file(filename):
                file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            else:
                flash('Разрешенные типы файлов - png, jpg, jpeg, gif. К сожалению рецепт не добавлен, попробуйте ещё раз.')
                return redirect(url_for('.add_recipe'))
        new_recipe = Recipe(title=form.title.data,
                            image_recipe = filename,
                            decription_recipe = form.decription_recipe.data,
                            ingredients = form.ingredients.data,
                            steps_recipe = form.steps_recipe.data,
                            servings = form.servings.data,
                            time_cooking = form.time_cooking.data,
                            user_id=current_user.id
                            )
        try:
            db.session.add(new_recipe)
            db.session.commit()
            flash('Рецепт успешно добавлен!')
            return redirect(url_for('index'))
        except Exception as exc:
            print("Error:", exc)
            return f"При добавлении рецепта произошла ошибка."
    return render_template('add_recipe.html', form=form)
    
@blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.filter(Recipe.id==id).first()
    form = EditRecipeForm()
    if form.validate_on_submit() and request.method == 'POST':
        recipe.title = form.title.data 
        recipe.decription_recipe = form.decription_recipe.data
        recipe.ingredients = form.ingredients.data
        recipe.steps_recipe = form.steps_recipe.data
        recipe.servings = form.servings.data
        recipe.time_cooking = form.time_cooking.data
        
        file = form.image_recipe.data
        filename = secure_filename(file.filename)
        if file:
            if allowed_file(filename):
                file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
                recipe.image_recipe = filename
            else:
                flash('Разрешенные типы файлов - png, jpg, jpeg, gif. К сожалению фото рецепта не загружено, попробуйте ещё раз.')
                return redirect(url_for('.edit_recipe', id=id))
        try:
            db.session.commit()
            flash('Рецепт успешно обновлён!')
            return redirect('/')
        except Exception as exc:
            print("Error:", exc)
            return f"При редактировании рецепта произошла ошибка."
    form = EditRecipeForm(obj=recipe)
    return render_template('edit_recipe.html', recipe=recipe, form=form)
    
@blueprint.route('/delete/<int:id>')
@login_required
def recipe_delete(id):
    recipe = Recipe.query.get_or_404(id)
    try:
        db.session.delete(recipe)
        db.session.commit()
        flash('Рецепт удален!')
        return redirect('/')
    except:
        return 'При удалении рецепта произошла ошибка'
    
@blueprint.route('/my')
@login_required
def my_recipes():
    user = Recipe.query.filter(Recipe.user_id == current_user.id).count()
    if user:
        recipes_list = Recipe.query.order_by(Recipe.created_at.desc()).all()
        return render_template('my_recipes.html', recipes_list=recipes_list)
    flash('Вы пока не добавили ни одного рецепта. Скорей переходи в категорию "Добавить рецепт"')
    return redirect(url_for('index'))

        
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

    
