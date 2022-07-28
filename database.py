from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)


    def __repr__(self):
        return f'<Post #{self.id} ("{self.title}" by {self.userId})>'

    def data(self):
        return {
            "id" : self.id,
            "userId" : self.userId,
            "title" : self.title,
            "body" : self.body
        }
