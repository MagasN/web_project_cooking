from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Date
from db import Base, engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_user = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    is_deleted = Column(Boolean)
    
    def __repr__(self):
        return f'<User id: {self.id}, name: {self.full_name}>'

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment = Column(String)
    created_at = Column(DateTime)
    is_deleted = Column(Boolean)
    user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    
    
    def __repr__(self):
        return f'<Comment id: {self.id}, text: {self.comment}>'
    
class Unit(Base):
    __tablename__ = 'units_measure'

    id = Column(Integer, primary_key=True)
    unit_name = Column(String)
   
    def __repr__(self):
        return f'Unit id: {self.id}, name: {self.unit_name}'
    
class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    ingredient_name = Column(String)
    ingredient_quantily = Column(String)
    unit_id = Column(Integer, ForeignKey(Unit.id), index=True, nullable=False)

    def __repr__(self):
        return f'Ingredient id: {self.id}, name: {self.ingredient_name}'
    
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    image_recipe = Column(String)
    decription_recipe = Column(String)
    steps_recipe = Column(Text, nullable=False)
    positive_feedback = Column(Integer)
    negative_feedback = Column(Integer)
    servings = Column(Integer, nullable=False)
    time_cooking = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    is_deleted = Column(Boolean)
    is_archived = Column(Boolean) 
    archived_at = Column(Boolean) 
    comment_id = Column(Integer, ForeignKey(Comment.id), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey(Ingredient.id), index=True, nullable=False)

    def __repr__(self):
        return f'Recipe id: {self.id}, title: {self.title}'
    
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)