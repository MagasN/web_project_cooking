from flask import abort, Blueprint, current_app, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required

from app.recipe.forms import AddRecipeForm, EditRecipeForm, CommentForm
from app.recipe.models import Comment, Unit, Ingredient, Recipe
from app.user.models import User
from app.model import db
from app.utils import get_redirect_target


blueprint = Blueprint('recipe', __name__, url_prefix='/recipes')

@blueprint.route('/top')
def top_recipes():
    # user = User.query.filter_by(id=Recipe.user_id).first_or_404()
    # Нужно доделать вывод автора рецепта, дату и т.п.
    recipes_list = Recipe.query.order_by(Recipe.positive_feedback.desc()).all()
    return render_template('top_recipes.html', recipes_list=recipes_list)
    
@blueprint.route('/<int:id>')
def recipe_page(id):
    recipe = Recipe.query.get(id)
    # user = User.query.filter_by(id=Recipe.user_id).first()
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
    
@blueprint.route('/add')
def add_recipe():
    # Нужно доделать
    add_recipe_form = AddRecipeForm()
    return render_template('add_recipe.html', form=add_recipe_form)
    
@blueprint.route('/process-add-recipe', methods=['POST'])
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
    
@blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.filter(Recipe.id==id).first()

    if request.method == 'POST':
        form = EditRecipeForm(formdata=request.form, obj=recipe)
        form.populate_obj(recipe)
        db.session.commit()
        flash('Рецепт успешно обновлён!')
        return redirect(url_for('index'))
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
    