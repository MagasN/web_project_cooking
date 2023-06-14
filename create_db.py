from webapp import db, create_app


with create_app().app_context():
    db.create_all()