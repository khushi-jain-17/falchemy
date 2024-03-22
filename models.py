from __init__ import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)

    # def __repr__(self):
    #     # return "<Blog %r>" % self.title
    #     return f'<Blog {self.title} >'


