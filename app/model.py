from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    image_recipe = db.Column(db.String)
    decription_recipe = db.Column(db.String)
    steps_recipe = db.Column(db.Text, nullable=False)
    positive_feedback = db.Column(db.Integer)
    negative_feedback = db.Column(db.Integer)
    servings = db.Column(db.Integer, nullable=False)
    time_cooking = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean)
    is_archived = db.Column(db.Boolean) 
    archived_at = db.Column(db.Boolean) 
    comment_id = db.Column(db.Integer, db.ForeignKey(db.Comment.id), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(db.User.id), index=True, nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(db.Ingredient.id), index=True, nullable=False)

    def __repr__(self):
        return f'Recipe id: {self.id}, title: {self.title}'