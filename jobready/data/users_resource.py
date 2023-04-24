from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.users import User


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f'User {user_id} not found')


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict()})


class UsersListResource(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            avatar=args.get('avatar'),
            username=args.get('username'),
            bio=args.get('bio'),
            email=args.get('email'),
            hashed_password=args.get('hashed_password'),
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('avatar', type=str)
parser.add_argument('username', required=True, type=str)
parser.add_argument('bio', type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('hashed_password', required=True, type=str)
