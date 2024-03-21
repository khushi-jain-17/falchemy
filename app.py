from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

from route import my_routes
app.register_blueprint(my_routes)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)

    # def __repr__(self):
    #     # return "<Blog %r>" % self.title
    #     return f'<Blog {self.title} >'
    
if __name__ == '__main__':
    app.run(debug=True)
