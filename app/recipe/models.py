from datetime import datetime
from sqlalchemy.orm import relationship

from app.user.models import User

from app.db import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), index=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id", ondelete="CASCADE"), index=True)

    recipe = relationship("Recipe", backref="comment")
    user = relationship("User", backref="comment")

    def __repr__(self):
        return f"<Comment id: {self.id}, text: {self.comment}>"


class Unit(db.Model):
    __tablename__ = "units_measure"

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Unit id: {self.id}, name: {self.unit_name}"


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String, nullable=False)
    ingredient_quantily = db.Column(db.String, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("units_measure.id", ondelete="CASCADE"), index=True)

    def __repr__(self):
        return f"Ingredient id: {self.id}, name: {self.ingredient_name}"


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    image_recipe = db.Column(db.String)
    decription_recipe = db.Column(db.String)
    steps_recipe = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)  # временное поле пока не реализовано задуманное
    positive_feedback = db.Column(db.Integer)
    negative_feedback = db.Column(db.Integer)
    servings = db.Column(db.Integer, nullable=False)
    time_cooking = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean)
    is_archived = db.Column(db.Boolean)
    archived_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), index=True)
    
    user = relationship("User", backref="recipe")

    def comments_count(self):
        return Comment.query.filter(Comment.recipe_id == self.id).count()

    def __repr__(self):
        return f"Recipe id: {self.id}, title: {self.title}, img: {self.image_recipe}"
