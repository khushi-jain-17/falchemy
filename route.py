from flask import request, jsonify, Blueprint
from models import Blog 
from datetime import datetime
from __init__ import db 

my_routes = Blueprint("my_routes", __name__)

@my_routes.route("/get", methods=["GET"])
def get():
    blogs = Blog.query.all()
    output = []
    for p in blogs:
        blog_data = {
            "id": p.id,
            "title": p.title,
            "author": p.author,
            "date_posted": p.date_posted
        }
        output.append(blog_data)
    return jsonify({"blogs": output})


@my_routes.route("/get_id", methods=['GET'])
def get_id():
    blog = Blog.query.get_or_404(id)
    return jsonify({"blog": blog})


@my_routes.route("/create", methods=['POST'])
def create():
    title = request.json["title"]
    author = request.json["author"]
    blog = Blog(title=title, author=author, date_posted=datetime.now())
    db.session.add(blog)
    db.session.commit()
    return jsonify({'message': 'blog created successfully'}), 201


@my_routes.route("/update/<int:id>", methods=['PUT'])
def update(id):
    blog = Blog.query.get_or_404(id)
    blog.title = request.json["title"]
    blog.author = request.json["author"]
    db.session.commit()
    return jsonify({'message': 'task updated successfully'})


@my_routes.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    blog_to_delete = Blog.query.get_or_404(id)
    db.session.delete(blog_to_delete)
    db.session.commit()
    return jsonify({'message': 'blog deleted'})


# @my_routes.route("/blog/<int:page_num>", methods=['GET'])
# def blog(page_num):
#     blogs = Blog.query.paginate(per_page=20, page=page_num, error_out=True)
#     return blogs 


