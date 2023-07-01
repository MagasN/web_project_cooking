from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# При распределении перенести class User в папку User.model, поменять пути
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    image_user = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String, default='user', index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<User id: {self.id}, name: {self.full_name}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), index=True, nullable=False)
    
    def __repr__(self):
        return f'<Comment id: {self.id}, text: {self.comment}>'

class Unit(db.Model):
    __tablename__ = 'units_measure'

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String, nullable=False)
   
    def __repr__(self):
        return f'Unit id: {self.id}, name: {self.unit_name}'

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String, nullable=False)
    ingredient_quantily = db.Column(db.String, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey(Unit.id), index=True, nullable=False)

    def __repr__(self):
        return f'Ingredient id: {self.id}, name: {self.ingredient_name}'

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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean)
    is_archived = db.Column(db.Boolean) 
    archived_at = db.Column(db.DateTime) 
    comment_id = db.Column(db.Integer, db.ForeignKey(Comment.id), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), index=True, nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredient.id), index=True, nullable=False)

    def __repr__(self):
        return f'Recipe id: {self.id}, title: {self.title}'