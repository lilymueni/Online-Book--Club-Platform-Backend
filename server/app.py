#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, User, BookClub, Membership, Discussion

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# CRUD for Users
class Users(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.get_json()
        new_user = User(
            username=data['username'],
            password_hash=data['password_hash'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

class UserByID(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    def put(self, user_id):
        data = request.get_json()
        user = User.query.get_or_404(user_id)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password_hash = data.get('password_hash', user.password_hash)
        db.session.commit()
        return jsonify(user.to_dict())

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

# CRUD for BookClubs
class BookClubs(Resource):
    def get(self):
        book_clubs = BookClub.query.all()
        return jsonify([book_club.to_dict() for book_club in book_clubs])

    def post(self):
        data = request.get_json()
        new_book_club = BookClub(
            name=data['name'],
            description=data['description'],
            cover_image=data['cover_image'],
            admin_id=data['admin_id']
        )
        db.session.add(new_book_club)
        db.session.commit()
        return jsonify(new_book_club.to_dict()), 201

class BookClubByID(Resource):
    def get(self, book_club_id):
        book_club = BookClub.query.get_or_404(book_club_id)
        return jsonify(book_club.to_dict())

    def put(self, book_club_id):
        data = request.get_json()
        book_club = BookClub.query.get_or_404(book_club_id)
        book_club.name = data.get('name', book_club.name)
        book_club.description = data.get('description', book_club.description)
        book_club.cover_image = data.get('cover_image', book_club.cover_image)
        db.session.commit()
        return jsonify(book_club.to_dict())

    def delete(self, book_club_id):
        book_club = BookClub.query.get_or_404(book_club_id)
        db.session.delete(book_club)
        db.session.commit()
        return '', 204

# CRUD for Discussions
class Discussions(Resource):
    def get(self):
        discussions = Discussion.query.all()
        return jsonify([discussion.to_dict() for discussion in discussions])

    def post(self):
        data = request.get_json()
        new_discussion = Discussion(
            content=data['content'],
            user_id=data['user_id'],
            book_club_id=data['book_club_id']
        )
        db.session.add(new_discussion)
        db.session.commit()
        return jsonify(new_discussion.to_dict()), 201

class DiscussionByID(Resource):
    def get(self, discussion_id):
        discussion = Discussion.query.get_or_404(discussion_id)
        return jsonify(discussion.to_dict())

    def put(self, discussion_id):
        data = request.get_json()
        discussion = Discussion.query.get_or_404(discussion_id)
        discussion.content = data.get('content', discussion.content)
        db.session.commit()
        return jsonify(discussion.to_dict())

    def delete(self, discussion_id):
        discussion = Discussion.query.get_or_404(discussion_id)
        db.session.delete(discussion)
        db.session.commit()
        return '', 204

api.add_resource(Users, '/users')
api.add_resource(UserByID, '/users/<int:user_id>')
api.add_resource(BookClubs, '/book_clubs')
api.add_resource(BookClubByID, '/book_clubs/<int:book_club_id>')
api.add_resource(Discussions, '/discussions')
api.add_resource(DiscussionByID, '/discussions/<int:discussion_id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
