from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, fresh_jwt_required
from models.post import PostModel
from schemas.post import PostSchema
from libs.strings import gettext

post_schema = PostSchema()
post_list_schema = PostSchema(many=True)


class Post(Resource):
    @classmethod
    def get(cls, name: str):
        post = PostModel.find_by_name(name)
        if post:
            return post_schema.dump(post), 200

        return {"message": gettext("post_not_found")}, 404

    @classmethod
#    @fresh_jwt_required
    def post(cls, name: str):
        if PostModel.find_by_name(name):
            return {"message": gettext("post_name_exists").format(name)}, 400

        post_json = request.get_json()
        post_json["name"] = name

        post = post_schema.load(post_json)

        try:
            post.save_to_db()
        except:
            return {"message": gettext("post_error_inserting")}, 500

        return post_schema.dump(post), 201

    @classmethod
#    @jwt_required
    def delete(cls, name: str):
        post = PostModel.find_by_name(name)
        if post:
            post.delete_from_db()
            return {"message": gettext("post_deleted")}, 200

        return {"message": gettext("post_not_found")}, 404

    @classmethod
    def put(cls, name: str):
        post_json = request.get_json()
        post = PostModel.find_by_name(name)

        if post:
            post.description = post_json["description"]
        else:
            post_json["name"] = name
            post = post_schema.load(post_json)

        post.save_to_db()

        return post_schema.dump(post), 200


class PostList(Resource):
    @classmethod
    def get(cls):
        return {"posts": post_list_schema.dump(PostModel.find_all())}, 200
