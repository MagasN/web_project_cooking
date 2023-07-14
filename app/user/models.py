from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    image_user = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String, index=True, default='User')
    created_at = db.Column(db.DateTime)
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
