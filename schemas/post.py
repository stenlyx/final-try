from ma import ma
from models.post import PostModel


class PostSchema(ma.ModelSchema):
    class Meta:
        model = PostModel
        dump_only = ("id",)
