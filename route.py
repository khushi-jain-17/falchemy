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


@my_routes.route("/get_id/<int:id>", methods=['GET'])
def get_id(id):
    blogs = Blog.query.get_or_404(id)
    output = []
    blog_data = {
        "id": blogs.id,
        "title": blogs.title,
        "author": blogs.author,
        "date_posted": blogs.date_posted
    }
    output.append(blog_data)
    return jsonify({"blogs": output})


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


@my_routes.route("/blog/<int:page_num>", methods=['GET'])
def blog(page_num):
    blogs = Blog.query.paginate(per_page=17, page=page_num, error_out=True)
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


@my_routes.route("/blogs", methods=['GET'])
def myblog():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    blogs = Blog.query.paginate(
        page=page, per_page=per_page, error_out=True
    )
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
