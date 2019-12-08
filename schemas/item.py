from ma import ma
from models.item import ItemModel


class ItemSchema(ma.ModelSchema):
    class Meta:
        model = ItemModel
        dump_only = ("id",)
        include_fk = True
